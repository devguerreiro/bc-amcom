from django.contrib import admin

from dunder_mifflin.core.domain.entity.client import Client
from dunder_mifflin.core.domain.entity.commission import CommissionLimit
from dunder_mifflin.core.domain.entity.product import Product
from dunder_mifflin.core.domain.entity.sale import Sale, SaleItem
from dunder_mifflin.core.domain.entity.seller import Seller

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Seller)
admin.site.register(CommissionLimit)
admin.site.register(Sale)
admin.site.register(SaleItem)
