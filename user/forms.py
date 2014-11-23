from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings

from app.utils import send_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout
from crispy_forms.layout import HTML
from crispy_forms.layout import ButtonHolder
from captcha.fields import ReCaptchaField


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', u'Entrar'))


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', u'Enviar'))

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None,
             html_email_template_name=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
        User = get_user_model()
        active_users = User.objects.filter(email__iexact=email, is_active=True)
        for user in active_users:
            subject = u'Gecolsa - Restablecer la contraseña'
            send_email(
                subject,
                [user.email],
                email_template_name,
                {
                    'email': user.email,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': token_generator.make_token(user),
                    'protocol': settings.PROTOCOL,
                },
            )


class CustomSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', u'Cambiar mi contraseña'))


class UserRegistrationForm(forms.ModelForm):
    is_accepted = forms.BooleanField(
        label=u'Acepto los terminos aquí contenidos para trabajar con nosotros',
    )
    captcha = ReCaptchaField()

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            HTML(u'''
                El titular de la información que diligencie el formulario de
                nuestro de este link _____________________________
                (Dirección URL del site de SATISFACCIÓN AL CLIENTE/QUEJAS Y
                RECLAMOS. "SATISFACCiON AL CUENTE/QUEJAS Y RECLAMOS",
                manifiesta en forma libre y expresa que los datos personales e
                información suministrada, está aceptando y autorizando
                a GECOLSA para que incluya esta información en su base de
                datos y pueda hacer uso de la misma para efectos de estudios
                de mercados, publicidad, compartir con fábrica o cualquier
                otro tipo de uso comercial propio de la Compañia, bajo
                la normatividad vigente y la politica de Tratamiento de
                la Información y Datos Personales de GECOLSA (Link: legal).
                El Titular de la información podrá en cualquier momento
                aclarar, completar, rectificar o solicitar la eliminación de
                esta información, contactándose al correo electrónico:
                comunicados@gecolsa.com.co.
            '''),
            'is_accepted',
            'captcha',
            ButtonHolder(
                Submit('submit', u'Suscribirse'),
            )
        )
