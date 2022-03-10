from django.shortcuts import render

from rest_framework import viewsets, views
from rest_framework.filters import SearchFilter
from cocktails.serializers import (
    CocktailSerializer,
)
from cocktails.models import (
    Cocktail,
)


# Create your views here.

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        """ /?search='SEARCH_BY_NAME'&base='SEARCH_BY_BASE'"""
        queryset = super().get_queryset()
        base = self.request.query_params.get('base')
        if base is not None:
            queryset = queryset.filter(base__name__iexact=base)
        return queryset
