# Generated by Django 5.0.3 on 2024-03-30 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_contactus_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='address',
        ),
    ]
