from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAccountTests(TestCase):
    def test_create_user(self):
        email = 'test@example.com'
        password = 'password123'
        user = User.objects.create_user(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertIsNone(user.role)
        self.assertTrue(user.is_active)
    
    def test_create_superuser(self):
        email = 'admin@example.com'
        password = 'adminpassword123'
        user = User.objects.create_superuser(email=email, password=password)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.role, 'Administrador')
        self.assertTrue(user.is_active)

    def test_get_full_name(self):
        user = User.objects.create_user(email='test@example.com', password='password123', first_name='John', last_name='Doe')
        full_name = user.get_full_name()
        
        self.assertEqual(full_name, 'John Doe')
    
    def test_str(self):
        username = 'testuser'
        user = User.objects.create_user(email='test@example.com', password='password123', username=username)
        user_str = str(user)
        
        self.assertEqual(user_str, username)
