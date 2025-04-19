from rest_framework import serializers
from .models import TodoItemEntity


class ToDoSerializer(serializers.ModelSerializer):


	class Meta:
   		model = TodoItemEntity
   		fields = '__all__'
