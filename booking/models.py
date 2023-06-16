from django.db import models


class Booking(models.Model):
    SIZE_OPTIONS = (
        (0, 'Small'),
        (1, 'Medium'),
        (2, 'Big'),
    )
    SHIFT_OPTIONS = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
    )

    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='E-mail')
    pet_name = models.CharField(verbose_name='Pet name', max_length=50)
    date = models.DateField(verbose_name='Date', help_text='mm/dd/yyyy')
    shift = models.CharField(verbose_name='Shift', max_length=10, choices=SHIFT_OPTIONS)
    size = models.IntegerField(verbose_name='Size', choices=SIZE_OPTIONS)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}: {self.date} - {self.shift}'

    class Meta:
        verbose_name = 'Bath booking'
        verbose_name_plural = 'Bath bookings'
    