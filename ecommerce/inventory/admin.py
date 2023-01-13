from django.contrib import admin
from ecommerce.inventory.models import Category

from . import models

admin.site.register(Category)

admin.site.register(models.Product)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


admin.site.register(models.ProductInventory, InventoryAdmin)
