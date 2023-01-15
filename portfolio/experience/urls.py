from django.urls import path
from rest_framework import routers
from .views import ExperienceViewSet,CompanyViewSet

router = routers.SimpleRouter()
router.register(prefix="experience", viewset=ExperienceViewSet)
router.register(prefix="company", viewset=CompanyViewSet)

urlpatterns = router.urls