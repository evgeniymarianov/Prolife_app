# Generated by Django 3.0.7 on 2020-09-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0005_auto_20200831_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.SlugField(default='shorts', max_length=160, unique=True),
            preserve_default=False,
        ),
    ]
