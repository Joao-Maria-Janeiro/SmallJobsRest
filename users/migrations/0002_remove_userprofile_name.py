# Generated by Django 2.2.12 on 2020-05-30 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
