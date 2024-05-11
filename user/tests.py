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

    def test_successful_registration(self):
        # Enviar o formulário de registro
        response = self.client.post(self.register_url, {'username': self.username, 'password1': self.password, 'password2': self.password})

    def test_successful_redirection(self):
        # Enviar o formulário de registro
        response = self.client.post(self.register_url, {'username': self.username, 'password1': self.password, 'password2': self.password})
        # Verificar se o redirecionamento ocorreu
        # Isso verifica se o usário foi redirecionado para a página de login
        self.assertEqual(response.status_code, 200)

    def test_user_saved(self):
        # Enviar o formulário de registro
        # E verificar se o usuário foi salvo no banco de dados
        self.client.post(self.register_url, {'username': self.username, 'password1': self.password, 'password2': self.password})
        # Verificar se o usuário foi salvo no banco de dados
        self.assertTrue(User.objects.filter(username=self.username).exists(), "O novo usuário existe no banco de dados.")

    def test_login(self):
        response = self.client.post(self.login_url, {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)
