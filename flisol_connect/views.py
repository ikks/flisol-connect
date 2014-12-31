#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['subscriptions'] = 12300
        context['volunteers'] = 876
        context['instances'] = 236

        return context
