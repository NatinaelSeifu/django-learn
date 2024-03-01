from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length = 256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basicapp:detail", kwargs={"pk": self.pk})

class Students(models.Model):
    name = models.CharField(max_length = 256)
    age = models.CharField(max_length=256)
    school = models.ForeignKey(School, on_delete = models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
    
    
    