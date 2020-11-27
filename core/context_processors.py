def maytok_context(request):
    return {'canonical_path': request.build_absolute_uri(request.path)}
