from django.contrib import admin

from paper.core.domain.entity.client import Client
from paper.core.domain.entity.product import CommissionPercentLimit, Product
from paper.core.domain.entity.seller import Seller

admin.site.register(Product)
admin.site.register(CommissionPercentLimit)
admin.site.register(Client)
admin.site.register(Seller)
