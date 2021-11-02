from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import User

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test User model if it is succesfull or not"""
        email="maneeshsagar97@gmail.com"
        password="12356"
        user=get_user_model().objects.create_user(
            email,
            password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_validation(self):
        """chacking for the eamil is is lower case or not"""
        email="maneeshsgar@GMAIL.COM"
        user=User.objects.create_user(
            email,
            "123")

        self.assertEqual(user.email,email.lower())

    def test_new_user_email_invalid(self):
        """Testing creating user"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None,'test12')

    def test_super_user_created(self):
        """Testing Super User"""
        user=User.objects.create_super_user(
            'maneeshsagar97@gmail.com',
            'test4'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
