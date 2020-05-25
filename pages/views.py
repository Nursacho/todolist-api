from .serializers import (
    TodoListSerializer,
    CategorySerializer,
    TodoListDetailSerializer,
    TodoListCreatSerializer,
)

from .models import Category, TodoList
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoListView(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TotoListDetailView(RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListDetailSerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TotoListCreateView(CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListCreatSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoListUpdateView(UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListCreatSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoListDestroyView(DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListDetailSerializer





