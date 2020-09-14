from django.contrib import admin

from .models import Category, GiftAddress, Gift, GiftShot, Comment
from crisis_line.models import Case, Nko, Task

from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class GiftAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Gift
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ("name", "email")


class GiftShotInline(admin.TabularInline):
    model = GiftShot
    extra = 1
    list_display = ("name", "get_image")
    readonly_fields = ("get_image",)


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "url", "new",)
    readonly_fields = ("get_image",)
    list_filter = ("category", "create_date")
    search_fields = ("title", "category__name")
    inlines = [GiftShotInline, CommentInline]
    save_on_top = True
    save_as = True
    list_editable = ("new",)
    actions = ["mark_as_new", "mark_as_not_new"]
    form = GiftAdminForm
    fieldsets = (
        (None, {
            "fields": (("title",),)
        }),
        (None, {
            "fields": ("description", ("photo", "get_image"))
        }),
        (None, {
            "fields": (("user",),)
        }),
        ("Address", {
            "classes": ("collapse",),
            "fields": (("address", "category"),)
        }),
        ("Options", {
            "fields": (("url", "new"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    def mark_as_not_new(self, request, queryset):
        """Отметить как б\у"""
        row_update = queryset.update(new=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def mark_as_new(self, request, queryset):
        """Отметить как новую"""
        row_update = queryset.update(new=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    mark_as_new.short_description = "Отметить как новую"
    mark_as_new.allowed_permissions = ('change', )

    mark_as_not_new.short_description = "Отметить как б\у"
    mark_as_not_new.allowed_permissions = ('change',)
    get_image.short_description = "Постер"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "gift", "id")
    readonly_fields = ("name", "email")


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(GiftShot)
class GiftShotAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "gift", "get_image")
    readonly_fields = ("get_image",)


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

        get_image.short_description = "Изображение"


admin.site.site_title = "Django Gifts"
admin.site.site_header = "Django Gifts"
admin.site.register(Case)
admin.site.register(Nko)
admin.site.register(Task)
