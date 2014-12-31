#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.utils.translation import ugettext as _

# from app.utils import send_email

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
        self.helper.add_input(Submit('submit', _('Login')))


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Send')))

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
            subject = _('Flisol - Restore your password')
            # send_email(
            #     subject,
            #     [user.email],
            #     email_template_name,
            #     {
            #         'email': user.email,
            #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #         'user': user,
            #         'token': token_generator.make_token(user),
            #         'protocol': settings.PROTOCOL,
            #     },
            # )


class CustomSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Change my password')))


class UserRegistrationForm(forms.ModelForm):
    is_accepted = forms.BooleanField(
        label=_('I accept the terms to join'),
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
            HTML(_('''We will not sell or use in other way your data,
                we ask the minimum amount to guarantee your privacy.
            ''')),
            'is_accepted',
            'captcha',
            ButtonHolder(
                Submit('submit', _('Join')),
            )
        )


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = (
            'avatar',
            'description',
            'first_name',
            'last_name',
        )

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'avatar',
            'first_name',
            'last_name',
            'description',
            ButtonHolder(
                Submit('submit', _('Update'), css_class="button"),
            )
        )
