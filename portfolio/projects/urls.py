from django.urls import path
from rest_framework import routers
from .views import ProjectsViewSet

router=routers.SimpleRouter()
router.register(prefix="projects",viewset=ProjectsViewSet)

urlpatterns=router.urls