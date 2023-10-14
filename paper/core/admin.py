from django.contrib import admin

from paper.core.domain.entity.client import Client
from paper.core.domain.entity.product import Product
from paper.core.domain.entity.seller import Seller

# from paper.core.domain.entity.sale import Sale
# from paper.core.domain.admin.sale import SaleAdmin

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Seller)

# admin.site.register(Sale, SaleAdmin)
