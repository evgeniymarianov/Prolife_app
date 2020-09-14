from django.db import models

class Nko(models.Model):
    """Некоммерческая организация"""
    title = models.CharField(max_length=150, verbose_name='Название организации')
    phone = models.CharField(max_length=30, verbose_name='Телефон организации')
    description = models.TextField("Описание организации")

    class Meta:
        verbose_name='Некоммерческую организацию'
        verbose_name_plural='Некоммерческие организации'

    def __str__(self):
        return self.title


class Case(models.Model):
    """Поступившее обращение"""
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата обращения')
    name = models.CharField(max_length=50, verbose_name='Имя обратившейся')
    phone = models.CharField(max_length=30, verbose_name='Телефон обратившейся')
    email = models.EmailField()
    description = models.TextField("Описание обращения")

    class Meta:
        verbose_name='Обращение'
        verbose_name_plural='обращения'

    def __str__(self):
        return str(self.create_date)


class Task(models.Model):
    """Задача по обращению"""
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата обращения')
    description = models.TextField("Описание задачи")
    status = models.CharField(choices = (
            ('Назначена дата обратной связи', 'Назначена дата обратной связи'),
            ('Ожидает обратной связи', 'Ожидает обратной связи'),
            ('Задача выполнена', 'Задача выполнена'),
        ),
        max_length=40, verbose_name='Статус задачи'
    )
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)
    nko = models.ForeignKey(Nko, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name='Задачу по обращению'
        verbose_name_plural='Задачи по обращению'

    def __str__(self):
        return str(self.create_date)
