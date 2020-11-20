from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=300)
    date_created = models.DateTimeField()
