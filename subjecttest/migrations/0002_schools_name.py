# Generated by Django 4.0 on 2023-10-14 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjecttest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schools',
            name='name',
            field=models.CharField(default='maktab 1', max_length=200),
        ),
    ]
