# Generated by Django 3.0.7 on 2020-08-31 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0004_auto_20200831_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='newness',
            new_name='new',
        ),
    ]