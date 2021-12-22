from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)


class OsPlatform(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    is_free = models.BooleanField()
    description = models.TextField(
        max_length=1000, default='OS platform description', validators=[MinLengthValidator(10)])

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    description = models.TextField(
        max_length=1000, default='Service description', validators=[MinLengthValidator(10)])
    os_platform = models.ManyToManyField(OsPlatform, related_name='services')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]
