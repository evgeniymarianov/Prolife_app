# Generated by Django 3.0.7 on 2020-08-28 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
    ]