#! /usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date

from django.views.generic.base import TemplateView

from flisol_event.models import FlisolEvent


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['subscriptions'] = 12300
        context['volunteers'] = 876
        context['instances'] = 236
        days_to_go = (
            FlisolEvent.objects.latest('id').official_date -
            date.today()
        ).days
        context['days_to_go'] = None
        if days_to_go >= 0:
            context['days_to_go'] = days_to_go

        return context
