from rest_framework import routers

from paper.core.infra.views.client import ClientView
from paper.core.infra.views.product import ProductView
from paper.core.infra.views.seller import SellerView

router = routers.DefaultRouter()

router.register("client", ClientView, basename="client")
router.register("seller", SellerView, basename="seller")
router.register("product", ProductView, basename="product")
