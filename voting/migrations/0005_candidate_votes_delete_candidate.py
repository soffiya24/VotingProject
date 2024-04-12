# Generated by Django 4.2.8 on 2024-04-03 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_remove_contactus_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_votes',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('votes', models.IntegerField(max_length=100)),
                ('Election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.election')),
            ],
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
    ]
