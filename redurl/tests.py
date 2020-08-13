from django.test import TestCase
from users.models import CustomUser
from redurl.models import RedUrl, Click
from rest_framework.test import APIClient
from django.utils import timezone
from django.db import IntegrityError
# Create your tests here.
class RedUrlTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='test_user', email='email@email.email', password='password1')
    
    def test_check_created_no_user(self):
        time = timezone.now()
        RedUrl.objects.create(url='https://www.url1.com', ip_creator='127.0.0.1', created=time)
        obj = RedUrl.objects.get(id=1)
        self.assertEqual(obj.url, 'https://www.url1.com')
        self.assertEqual(obj.ip_creator, '127.0.0.1')
        self.assertEqual(obj.created, time)
    
    def test_check_created_user(self):
        time = timezone.now()
        self.user.slugs.add(RedUrl.objects.create(user_creator=self.user,url='https://www.url2.com', ip_creator='127.0.0.1', created=time))
        obj = RedUrl.objects.get(id=1)
        self.assertEqual(obj.url, 'https://www.url2.com')
        self.assertEqual(obj.ip_creator, '127.0.0.1')
        self.assertEqual(obj.created, time)
        self.assertEqual(obj, self.user.slugs.first())
    
    def getClient(self):
        client = APIClient()
        client.login(username=self.user.username, password='password1')
        return client

    def test_bad_create(self):
        with self.assertRaises(IntegrityError):
            RedUrl.objects.create()
    def test_create_bad(self):

        with self.assertRaises(IntegrityError):
            RedUrl.objects.create(slug="hello")
    
    def test_api_create_nouser(self):
        client = APIClient()
        response = client.post("/api/create/", {"url": "https://www.djangoproject.com"})
        self.assertEqual(response.status_code, 201)
        response1 = client.post("/api/create/", {"url": "https://www.djangoproject.com", "slug": "djagnofoundation"})
        self.assertEqual(response1.status_code, 401)
        response2 = client.post("/api/create/", {})
        self.assertEqual(response2.status_code, 400)

    def test_api_create_user(self):
        client = self.getClient()
        response = client.post("/api/create/", {"url": "https://www.djangoproject.com"})
        self.assertEqual(response.status_code, 201)
        response1 = client.post("/api/create/", {"url": "https://www.djangoproject.com", "slug": "djagnofoundation"})
        self.assertEqual(response1.status_code, 201)
        response2 = client.post("/api/create/", {"url": "https://www.djangoproject.com", "slug": "djagnofoundation"})
        self.assertEqual(response2.status_code, 400)
        response3 = client.post("/api/create/", {})
        self.assertEqual(response3.status_code, 400)
