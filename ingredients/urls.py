from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from ingredients import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]