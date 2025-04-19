from rest_framework import serializers
from .models import TodoItemEntity


from rest_framework import serializers
from .models import TodoItemEntity, Category


class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
   category_id = serializers.PrimaryKeyRelatedField(
       queryset=Category.objects.all(), source='category', write_only=True, required=False)

   class Meta:
       model = TodoItemEntity
       fields = ['id', 'name', 'category_id']

   def to_representation(self, instance):
       rep = super().to_representation(instance)
       rep['category'] = CategorySerializer(instance.category).data if instance.category else None
       return rep



