# Generated by Django 2.2.12 on 2020-05-30 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200530_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='localizacao',
            new_name='location',
        ),
    ]
