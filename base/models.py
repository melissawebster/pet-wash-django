from django.core.exceptions import ValidationError
from django.db import models


class Contact(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='E-mail', max_length=50)
    message = models.TextField(verbose_name='Message')
    data = models.DateTimeField(verbose_name='Date sent', auto_now_add=True)
    def __str__(self):
        return f'{self.name} [{self.email}]'
    
    class Meta:
        verbose_name = 'Contact form'
        verbose_name_plural = 'Contact forms'
        ordering = ['-data']

def validate_cellphone_length(value):
    if len(str(value)) > 11:
        raise ValidationError('It should have at most 11 digits.')


class Booking(models.Model):
    petname = models.CharField(max_length=50)
    cellphone = models.IntegerField(validators=[validate_cellphone_length])
    bathday = models.DateField() 
    comments = models.TextField()
    def __str__(self):
        return f'{self.petname} [{self.bathday}]'