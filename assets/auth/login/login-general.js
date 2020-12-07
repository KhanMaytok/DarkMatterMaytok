"use strict";
var KTLogin = function () {
    var t, i = function (i) {
        var o = "login-" + i + "-on";
        i = "kt_login_" + i + "_form";
        t.removeClass("login-forgot-on"), t.removeClass("login-signin-on"), t.removeClass("login-signup-on"), t.addClass(o), KTUtil.animateClass(KTUtil.getById(i), "animate__animated animate__backInUp")
    };
    return {
        init: function () {
            var o;
            t = $("#kt_login"), o = FormValidation.formValidation(KTUtil.getById("kt_login_signin_form"), {
                fields: {
                    username: {validators: {notEmpty: {message: "No has ingresado usuario"}}},
                    password: {validators: {notEmpty: {message: "No has ingresado contraseña"}}}
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger,
                    submitButton: new FormValidation.plugins.SubmitButton,
                    bootstrap: new FormValidation.plugins.Bootstrap
                }
            }), $("#kt_login_signin_submit").on("click", (function (t) {
                t.preventDefault(), o.validate().then((function (t) {
                    if (t == "Valid") {
                        console.log("Ingresando...")
                        $('#kt_login_signin_form').submit();
                    } else {
                        alert("Hay errores. corrígelos por favor");
                    }
                }))
            })), $("#google_login").on("click", (function (t) {
                location.href = google_login_url;
            })), $("#facebook_login").on("click", (function (t) {
                location.href = facebook_login_url;
            })), $("#kt_login_forgot").on("click", (function (t) {
                t.preventDefault(), i("forgot")
            })), $("#kt_login_signup").on("click", (function (t) {
                t.preventDefault(), i("signup")
            })), function (t) {
                var o, n = KTUtil.getById("kt_login_signup_form");
                o = FormValidation.formValidation(n, {
                    fields: {
                        username: {validators: {notEmpty: {message: "No has ingresado usuario"}}},
                        email: {
                            validators: {
                                notEmpty: {message: "No has ingresado un email"},
                                emailAddress: {message: "Esto no parece un email"}
                            }
                        },
                        password1: {validators: {notEmpty: {message: "Se requiere un password"}}},
                        password2: {
                            validators: {
                                notEmpty: {message: "Confirma la contraseña por favor"},
                                identical: {
                                    compare: function () {
                                        return n.querySelector('[name="password"]').value
                                    }, message: "Las contraseñas no son iguales"
                                }
                            }
                        },
                        agree: {validators: {notEmpty: {message: "Debes aceptar los términos y condiciones"}}}
                    },
                    plugins: {
                        trigger: new FormValidation.plugins.Trigger,
                        bootstrap: new FormValidation.plugins.Bootstrap
                    }
                }), $("#kt_login_signup_submit").on("click", (function (t) {
                    t.preventDefault(), o.validate().then((function (t) {
                        if (t == "Valid") {
                            console.log("Registrando...")
                            $('#kt_login_signup_form').submit();
                        } else {
                            alert("Hay errores. corrígelos por favor");
                        }
                    }))
                })), $("#kt_login_signup_cancel").on("click", (function (t) {
                    t.preventDefault(), i("signin")
                }))
            }(), function (t) {
                var o;
                o = FormValidation.formValidation(KTUtil.getById("kt_login_forgot_form"), {
                    fields: {
                        email: {
                            validators: {
                                notEmpty: {message: "Email address is required"},
                                emailAddress: {message: "The value is not a valid email address"}
                            }
                        }
                    },
                    plugins: {
                        trigger: new FormValidation.plugins.Trigger,
                        bootstrap: new FormValidation.plugins.Bootstrap
                    }
                }), $("#kt_login_forgot_submit").on("click", (function (t) {
                    t.preventDefault(), o.validate().then((function (t) {
                        "Valid" == t ? KTUtil.scrollTop() : swal.fire({
                            text: "Sorry, looks like there are some errors detected, please try again.",
                            icon: "error",
                            buttonsStyling: !1,
                            confirmButtonText: "Ok, got it!",
                            customClass: {confirmButton: "btn font-weight-bold btn-light-primary"}
                        }).then((function () {
                            KTUtil.scrollTop()
                        }))
                    }))
                })), $("#kt_login_forgot_cancel").on("click", (function (t) {
                    t.preventDefault(), i("signin")
                }))
            }()
        }
    }
}();
jQuery(document).ready((function () {
    KTLogin.init()
}));