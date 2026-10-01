from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from student.models import Student


class AuthFlowTests(TestCase):
    def test_registration_form_needs_login(self):
        for name in ('register', 'home'):
            response = self.client.get(reverse(name))
            self.assertRedirects(
                response, f"{reverse('login')}?next={reverse(name)}"
            )

    def test_signup_then_login_opens_registration_form(self):
        self.client.post(reverse('saveuser'), {
            'username': 'ankit', 'password': 'Str0ng#Pass91', 'name': 'Ankit',
        })
        self.assertTrue(User.objects.filter(username='ankit').exists())
        response = self.client.post(reverse('loginvalidation'), {
            'username': 'ankit', 'password': 'Str0ng#Pass91',
        })
        self.assertRedirects(response, reverse('register'))

    def test_wrong_password_stays_on_login(self):
        User.objects.create_user('ankit', password='Str0ng#Pass91')
        response = self.client.post(reverse('loginvalidation'), {
            'username': 'ankit', 'password': 'wrong',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_logout_locks_form_again(self):
        User.objects.create_user('ankit', password='Str0ng#Pass91')
        self.client.login(username='ankit', password='Str0ng#Pass91')
        self.client.get(reverse('logout'))
        self.assertEqual(self.client.get(reverse('register')).status_code, 302)


class StudentRegistrationTests(TestCase):
    data = {
        'roll_no': '0187AD231001',
        'name': 'Test Student',
        'email': 'test@example.com',
        'phone': '9876543210',
        'gender': 'M',
        'dob': '2005-01-15',
        'course': 'CSE-AIDS',
        'address': 'Bhopal, Madhya Pradesh',
    }

    def setUp(self):
        User.objects.create_user('ankit', password='Str0ng#Pass91')
        self.client.login(username='ankit', password='Str0ng#Pass91')

    def test_register_page_loads(self):
        self.assertEqual(self.client.get(reverse('register')).status_code, 200)

    def test_student_is_saved(self):
        response = self.client.post(reverse('savestudent'), self.data)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(Student.objects.count(), 1)

    def test_duplicate_roll_no_rejected(self):
        self.client.post(reverse('savestudent'), self.data)
        response = self.client.post(reverse('savestudent'), self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.count(), 1)

    def test_bad_phone_rejected(self):
        bad = dict(self.data, phone='123')
        self.client.post(reverse('savestudent'), bad)
        self.assertEqual(Student.objects.count(), 0)
