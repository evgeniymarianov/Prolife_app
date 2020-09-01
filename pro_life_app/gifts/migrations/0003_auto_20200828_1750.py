# Generated by Django 3.0.7 on 2020-08-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0002_remove_category_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftaddress',
            name='gift',
        ),
        migrations.AddField(
            model_name='gift',
            name='address',
            field=models.ManyToManyField(to='gifts.GiftAddress', verbose_name='Адреса'),
        ),
    ]