from django.db import models

# Create your models here.
class Product(models.Model):
    p_name=models.CharField(max_length=30)
    p_price=models.FloatField()
    p_offer=models.CharField(max_length=20)

    def __str__(self):
        return self.p_name