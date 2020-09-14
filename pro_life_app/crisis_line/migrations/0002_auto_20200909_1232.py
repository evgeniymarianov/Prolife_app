# Generated by Django 3.0.7 on 2020-09-09 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crisis_line', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'verbose_name': 'Обращение', 'verbose_name_plural': 'обращения'},
        ),
        migrations.AlterModelOptions(
            name='nko',
            options={'verbose_name': 'Некоммерческую организацию', 'verbose_name_plural': 'Некоммерческие организации'},
        ),
        migrations.RemoveField(
            model_name='case',
            name='nko',
        ),
        migrations.AlterField(
            model_name='case',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обращения'),
        ),
        migrations.AlterField(
            model_name='case',
            name='description',
            field=models.TextField(verbose_name='Описание обращения'),
        ),
        migrations.AlterField(
            model_name='case',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Телефон обратившейся'),
        ),
        migrations.AlterField(
            model_name='nko',
            name='description',
            field=models.TextField(verbose_name='Описание организации'),
        ),
        migrations.AlterField(
            model_name='nko',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Телефон организации'),
        ),
        migrations.AlterField(
            model_name='nko',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название организации'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата обращения')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('status', models.CharField(choices=[('Назначена дата обратной связи', 'Назначена дата обратной связи'), ('Ожидает обратной связи', 'Ожидает обратной связи'), ('Задача выполнена', 'Задача выполнена')], max_length=40, verbose_name='Статус задачи')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crisis_line.Case')),
                ('nko', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crisis_line.Nko')),
            ],
            options={
                'verbose_name': 'Задачу по обращению',
                'verbose_name_plural': 'Задачи по обращению',
            },
        ),
    ]