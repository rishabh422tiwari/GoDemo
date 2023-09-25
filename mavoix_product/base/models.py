from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Product(models.Model):
    prod_id = models.IntegerField()
    serial_no = models.IntegerField(null=False)
    catagory = models.CharField(max_length=255, blank=False)
    family = models.CharField(max_length=255, default=True, blank=False)
    image = models.ImageField()
    short_desc = models.CharField(max_length=255, default="", blank=True)
    long_desc = models.TextField(default="", blank=True)
    specification = models.TextField(default="", blank=True)
    stock = models.IntegerField(
        validators=[MinValueValidator(0)]
        )
    batch_no = models.CharField(max_length=255, blank=False)
    certification = models.CharField(max_length=255, default="", blank=True)


