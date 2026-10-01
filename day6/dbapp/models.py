from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)


    def __str__(self):
        return self.client_name