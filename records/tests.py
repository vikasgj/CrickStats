from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
