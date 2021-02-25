from django.test import RequestFactory, TestCase
from django.urls import resolve
from .views import home

class IndexTests(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get('/buku')
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)