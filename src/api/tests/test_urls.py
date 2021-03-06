"""(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017"""

from django.test import TestCase
from django.urls import resolve, reverse


class UrlTestCase(TestCase):

    def test_urls(self):
        # test that the right url is generated
        url = reverse('apikey-list')
        self.assertEqual(url, '/v1/apikeys/')

        # test that the URL connect to the right view
        resolver = resolve('/v1/apikeys/')
        self.assertEqual(resolver.view_name, 'apikey-list')
