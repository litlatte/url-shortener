from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
class UsersManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', username='user1', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.username, 'user1')
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='', password='foo')
        with self.assertRaises(TypeError):
            User.objects.create_user(username='', password='foo')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', username='', password='foo')
            
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='normal@user.com', username='superuser1', password='foo')
        self.assertEqual(admin_user.email, 'normal@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.username, 'superuser1')
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email='super@user.com', password='foo', is_superuser=False)
        
            