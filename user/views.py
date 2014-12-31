#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext as _

from user.forms import UserRegistrationForm
from user.forms import UserUpdateForm

from braces.views import LoginRequiredMixin


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user


class UserRegistrationView(CreateView):
    model = get_user_model()
    template_name = 'registration/registration_form.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Welcome to Flisol'),
        )
        return super(UserRegistrationView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user/user_update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Your changes have been applied'),
        )
        return super(UserUpdateView, self).form_valid(form)
