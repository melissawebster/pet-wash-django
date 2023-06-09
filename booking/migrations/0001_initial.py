# Generated by Django 4.2.1 on 2023-06-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('pet_name', models.CharField(max_length=50, verbose_name='Pet name')),
                ('date', models.DateField(help_text='mm/dd/yyyy', verbose_name='Date')),
                ('shift', models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon')], max_length=10, verbose_name='Shift')),
                ('size', models.IntegerField(choices=[(0, 'Small'), (1, 'Medium'), (2, 'Big')], verbose_name='Size')),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Bath booking',
                'verbose_name_plural': 'Bath bookings',
            },
        ),
    ]
