from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=0)