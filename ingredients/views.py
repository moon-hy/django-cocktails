from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from ingredients.models import Ingredient
from ingredients.serializers import (
    IngredientSerializer,
)

# Create your views here.
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        """/?search='SEARCH_BY_NAME'&category='SEARCH_BY_CATEGORY'"""
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__name__iexact=category)
        return queryset
