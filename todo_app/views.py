"""
views.py
Tento soubor obsahuje view funkce nebo třídy, které obsluhují požadavky uživatelů.
Zpracovávají data, která jsou získána z modelů nebo jiných zdrojů, a vrací odpověď
uživateli (např. HTML stránku nebo JSON).
"""

from django.shortcuts import render
from .models import TodoItemEntity
from .serializers import ToDoSerializer
from rest_framework import viewsets


class TodoItemViewSet(viewsets.ModelViewSet):
   queryset = TodoItemEntity.objects.all()
   serializer_class = ToDoSerializer
