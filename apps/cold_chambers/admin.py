from django.contrib import admin
from .models import ColdChambers

# Register your models here.


class ColdChamberAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = (
        "name",
        "categories",
        "dimensions",
        "camera_price",
        "installation_price",
        "description",
    )
    list_filter = ("name", "categories", "dimensions", "camera_price")


admin.site.register(ColdChambers, ColdChamberAdmin)
