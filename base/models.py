from django.core.exceptions import ValidationError
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


def validate_cellphone_length(value):
    if len(str(value)) > 11:
        raise ValidationError('O número de telefone deve ter no máximo 11 dígitos.')


class Booking(models.Model):
    petname = models.CharField(max_length=50)
    cellphone = models.IntegerField(validators=[validate_cellphone_length])
    bathday = models.DateField() 
    comments = models.TextField()