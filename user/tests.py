from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthenticationTest(TestCase):
    def setUp(self):
        self.register_url = reverse('user:register')
        self.login_url = reverse('login')
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_registration(self):
        new_username = 'newuser'
        new_password = 'newpassword'
        response = self.client.post(self.register_url, {'username': new_username, 'password1': new_password, 'password2': new_password})
        self.assertEqual(response.status_code, 200, msg="O registro não redirecionou corretamente.")
        self.assertFalse(User.objects.filter(username=new_username).exists(), "O usuário já existe no banco de dados")

    def test_login(self):
        response = self.client.post(self.login_url, {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)
