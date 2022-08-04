from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='start')
    release_date = models.DateField(max_length=50)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)
