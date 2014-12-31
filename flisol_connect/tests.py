from django.test import TestCase
from django.core.urlresolvers import reverse


class GeneralTests(TestCase):

    def test_main_page(self):
        """Tests the visibility of the home"""
        result = self.client.get(reverse('home'))
        self.assertEqual(result.status_code, 200)
