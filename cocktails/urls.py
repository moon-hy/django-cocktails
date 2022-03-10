from django.urls import path, include
from rest_framework import routers

from cocktails.views import *

router = routers.DefaultRouter()
router.register(r'cocktails', CocktailViewSet)

urlpatterns = [
    path('', include(router.urls))
]
