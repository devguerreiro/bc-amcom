from django.contrib.admin import ModelAdmin, TabularInline

from paper.core.domain.entity.sale import SaleItem


class SaleItemInline(TabularInline):
    model = SaleItem
    extra = 0


class SaleAdmin(ModelAdmin):
    inlines = [SaleItemInline]
