from django.urls import path
from rest_framework import routers
from .views import EventsViewSet

router = routers.SimpleRouter()
router.register(prefix="events", viewset=EventsViewSet)
# router.register(prefix="clients", viewset=OfflineClientViewSet)

urlpatterns = router.urls
