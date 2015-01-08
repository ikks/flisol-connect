#! /usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date

from django.views.generic.base import TemplateView
from django.core.cache import cache

from flisol_event.models import FlisolEvent
from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolAttendance


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        latest_event = cache.get('current_event_id')
        days_to_go = cache.get('days_to_go')
        if not days_to_go:
            latest_event = FlisolEvent.objects.latest('id')
            days_to_go = (
                latest_event.official_date -
                date.today()
            ).days
            cache.set('days_to_go', days_to_go)
            cache.set('current_event_id', latest_event.id)
        if days_to_go >= 0:
            context['days_to_go'] = days_to_go

        instances = cache.get('instances')
        if not instances:
            instances = FlisolInstance.objects.filter(
                flisol_event=latest_event
            ).count()
            context['instances'] = instances
        subscriptions = cache.get('subscriptions')
        if not subscriptions:
            from django.contrib.auth import get_user_model
            subscriptions = get_user_model().objects.filter(
                is_active=True
            ).count()
            cache.set('subscriptions', subscriptions)
            context['subscriptions'] = subscriptions
        volunteers = cache.get('volunteers')
        if not volunteers:
            volunteers = FlisolAttendance.objects.exclude(
                role=FlisolAttendance.ATTENDANCE_CHOICES_VISITOR,
            ).filter(flisol_instance__flisol_event=latest_event).count()
            cache.set('volunteers', volunteers)
            context['volunteers'] = volunteers

        return context
