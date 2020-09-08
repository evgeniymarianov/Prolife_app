from django import template
from gifts.models import Category, Gift

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()

@register.inclusion_tag('gifts/tags/last_gift.html')
def get_last_gifts(count=5):
    gifts = Gift.objects.order_by("create_date")[:count]
    return {"last_gifts": gifts}
