#! /usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import timedelta
from datetime import date
from django.test import TestCase
from django.core.urlresolvers import reverse

from flisol_event.models import FlisolEvent

from django_dynamic_fixture import G


class GeneralTests(TestCase):

    def setUp(self):
        official_date = date.today() + timedelta(30)
        G(
            FlisolEvent,
            official_date=official_date,
        )

    def test_main_page(self):
        """Tests the visibility of the home"""
        result = self.client.get(reverse('home'))
        self.assertEqual(result.status_code, 200)
