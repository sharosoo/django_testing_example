import json

from django.test import TestCase
from django.urls import reverse

from simpleapp.models import Simple


class DRFTests(TestCase):

    def setUp(self):
        Simple.objects.get_or_create(
            title='title1',
            slug='slug1',
        )
        Simple.objects.get_or_create(
            title='title2',
            slug='slug2',
        )

        self.create_read_url = reverse('simpleapp:simple_rest_api')
        self.read_update_delete_url = reverse(
            'simpleapp:simple_rest_api',
            kwargs={'slug': 'slug1'}
        )

    def test_list(self):
        response = self.client.get(self.create_read_url)

        self.assertContains(response, 'title1')
        self.assertContains(response, 'title2')

    def test_detail(self):
        response = self.client.get(self.read_update_delete_url)
        data = json.loads(response.content)
        content = {'title': 'title1', 'slug': 'slug1',
                   'point': 0}
        self.assertEquals(data, content)


