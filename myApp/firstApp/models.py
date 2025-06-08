from django.db import models
from django.utils import timezone
# Create your models here.

class details(models.Model):
    gender_type = [("Male","Male"),("Female","Female"),("Others","Others")]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)
    gender = models.CharField(max_length=10,choices=gender_type)
    date_added = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.name
