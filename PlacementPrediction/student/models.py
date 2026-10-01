from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ('BTech AI & DS', 'BTech AI & DS'),
        ('BTech CSE', 'BTech CSE'),
        ('BTech IT', 'BTech IT'),
        ('BTech ECE', 'BTech ECE'),
        ('Other', 'Other'),
    ]
    roll_no = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.roll_no} - {self.name}'
