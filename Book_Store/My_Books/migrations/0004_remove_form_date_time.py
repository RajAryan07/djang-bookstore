# Generated by Django 3.2.4 on 2021-07-14 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_Books', '0003_form_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='date_time',
        ),
    ]
