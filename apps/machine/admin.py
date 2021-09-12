from django.contrib import admin
from .models import Machine, ImageMachine
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.


class ImageInline(admin.StackedInline):
    model = ImageMachine
    extra = 1
    fk_name = "machine"


class MachineAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = (
        "name",
        "mark",
        "price",
        "stock",
        "categories",
    )
    list_filter = ("name", "mark", "price", "categories")
    inlines = [ImageInline]


admin.site.register(Machine, MachineAdmin)
