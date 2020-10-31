from django.test import SimpleTestCase
from django.urls import reverse, resolve

from core.views import *

class TestUrls(SimpleTestCase):


	def test_index_url(self):
		url = reverse('index')
		self.assertEqual(resolve(url).func, index)