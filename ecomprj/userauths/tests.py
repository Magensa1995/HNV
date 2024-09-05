from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserAuthTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.username = 'admin'
        self.password = '123456'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        # Simulate logging in with the test user's credentials
        login_url = reverse('userauths:login')  # Assuming you have a 'login' URL name defined
        response = self.client.post(login_url, {
            'username': self.username,
            'password': self.password
        })
        
        # Check if the login was successful
        self.assertEqual(response.status_code, 302)  # Assuming successful login redirects
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        # First, login the user
        self.client.login(username=self.username, password=self.password)
        
        # Simulate logging out
        logout_url = reverse('userauths:logout')  # Assuming you have a 'logout' URL name defined
        response = self.client.get(logout_url)
        
        # Check if the logout was successful
        self.assertEqual(response.status_code, 302)  # Assuming successful logout redirects
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_credentials(self):
        # Attempt login with invalid credentials
        login_url = reverse('userauths:login')
        response = self.client.post(login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        
        # Check if the login failed
        self.assertEqual(response.status_code, 200)  # Login page should be reloaded
        self.assertFalse(response.wsgi_request.user.is_authenticated)
