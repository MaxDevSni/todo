"""
views.py
Tento soubor obsahuje view funkce nebo třídy, které obsluhují požadavky uživatelů.
Zpracovávají data, která jsou získána z modelů nebo jiných zdrojů, a vrací odpověď
uživateli (např. HTML stránku nebo JSON).
"""

from django.shortcuts import render
from .models import TodoItemEntity, Category
from .serializers import ToDoSerializer, CategorySerializer
from rest_framework import viewsets


class TodoItemViewSet(viewsets.ModelViewSet):
   queryset = TodoItemEntity.objects.all()
   serializer_class = ToDoSerializer


class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
