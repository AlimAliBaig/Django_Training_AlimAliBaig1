from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    COURSE_CHOICES = [
        ('CSE', 'B.Tech CSE'),
        ('CSE-AIDS', 'B.Tech CSE (AI & Data Science)'),
        ('IT', 'B.Tech IT'),
        ('ECE', 'B.Tech ECE'),
        ('ME', 'B.Tech Mechanical'),
        ('CE', 'B.Tech Civil'),
    ]

    roll_no = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    address = models.TextField()
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.roll_no
# Create your models here.
