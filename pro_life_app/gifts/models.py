from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

from django.urls import reverse


class User(AbstractUser):
    balance = models.IntegerField(null=False, default=1000)
    country = models.CharField(max_length=30, null=False, default='Russia')


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class GiftAddress(models.Model):
    """Адреса"""
    country = models.CharField("Страна", max_length=100)
    city = models.CharField("Город", max_length=100)
    street = models.CharField("Улица", max_length=100)
    house = models.IntegerField("Номер дома", default=0)
    description = models.TextField("Описание")

    def __str__(self):
        return "%s %s %s" % (self.street, self.city, self.house)

    class Meta:
        verbose_name = "Адреса"
        verbose_name_plural = "Адреса"


class Gift(models.Model):
    """Дары"""
    title = models.CharField("Название", max_length=100)
    create_date = models.DateTimeField(auto_now=True)
    description = models.TextField("Описание")
    photo = models.ImageField("Фото", upload_to="movies/")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gift_user")
    address = models.ManyToManyField(GiftAddress, verbose_name="Адреса")
    new = models.BooleanField("Новая", default=False)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gift_detail", kwargs={"slug": self.url})

    def get_comment(self):
        return self.comment_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Дар"
        verbose_name_plural = "Дары"


class GiftShot(models.Model):
    """Фото дара"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    gift = models.ForeignKey(Gift, verbose_name="Дар", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото дара"
        verbose_name_plural = "Фото дара"


class Comment(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    gift = models.ForeignKey(Gift, verbose_name="Дар", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.gift}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"
