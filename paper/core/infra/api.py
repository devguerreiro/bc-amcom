from rest_framework import routers

from paper.core.infra.views.client import ClientView

router = routers.DefaultRouter()
router.register("client", ClientView, basename="client")
