from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'todo', TodoItemViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [
   path('', include(router.urls)),
]

