from rest_framework import routers

from dunder_mifflin.core.infra.views.client import ClientView
from dunder_mifflin.core.infra.views.product import ProductView
from dunder_mifflin.core.infra.views.sale import SaleView
from dunder_mifflin.core.infra.views.seller import SellerView

router = routers.DefaultRouter()

router.register("client", ClientView, basename="client")
router.register("seller", SellerView, basename="seller")
router.register("product", ProductView, basename="product")
router.register("sale", SaleView, basename="sale")
