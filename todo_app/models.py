"""
models.py
Tento soubor definuje datové modely (třídy), které představují tabulky v databázi.
Každá třída v tomto souboru reprezentuje jednu tabulku a jednotlivé vlastnosti jsou
sloupce této tabulky.
"""

from django.db import models


class TodoItemEntity(models.Model):
   name = models.CharField(max_length=100)


   def __str__(self):
      return self.name

