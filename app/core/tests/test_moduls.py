from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        '''
        Test that a user is created succesffully
        '''
        email = 'myemail@gmail.com'
        password = 'pass123%'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''
        Test if the email for a new use is normalized
        '''
        email = 'myemail@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_creating_user_invalid_email(self):
        '''
        Test if the email is valid
        '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass123')

    def test_create_new_superuser(self):
        '''Test creating a new superuser'''
        user  = get_user_model().objects.create_superuser(
        'superuser.email@gmail.com',
        'superpass'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
