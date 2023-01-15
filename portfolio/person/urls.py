from django.urls import path
from rest_framework import routers
from .views import PersonViewSet

router=routers.SimpleRouter()
router.register(prefix="person",viewset=PersonViewSet)


urlpatterns=router.urls