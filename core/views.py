from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.signals import user_logged_out

from core.forms import SignUpForm
from core.models import User


def logout(request):
    user = getattr(request, 'user', None)
    if not getattr(user, 'is_authenticated', True):
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)
    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()

    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/login.html', {'jaja': form})


def send_mail(founder_email):
    from django.core.mail import EmailMessage
    from django.template.loader import get_template

    message = get_template("core/email/founder.html").render()

    mail = EmailMessage(
        subject="Descubre el Universo Maytok",
        body=message,
        from_email='no-reply@maytok.com',
        to=[founder_email],
        reply_to=['no-reply@maytok.com'],
    )
    mail.content_subtype = "html"
    mail.send()


def create_founder(request):
    guid = request.GET.get('guid')
    user = User.objects.get(guid=guid)
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)

    user.username = username
    user.set_password(password)
    user.save()

    return redirect('home')
