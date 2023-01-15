from django.urls import path
from rest_framework import routers
from .views import SkillsViewSet,ToolsViewSet

router=routers.SimpleRouter()

router.register(prefix="skills",viewset=SkillsViewSet)
router.register(prefix="tools",viewset=ToolsViewSet)

urlpatterns=router.urls