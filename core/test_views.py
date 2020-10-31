from django.test import TestCase, Client
from django.urls import reverse

from . import views 

class TestViews(TestCase):

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'core/index.html')