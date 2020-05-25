from rest_framework import serializers
from .models import Category, TodoList
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    """GET list Category"""

    class Meta:
        model = Category
        fields = ('id', 'name')


class TodoListSerializer(serializers.ModelSerializer):
    """GET list TodoList"""

    class Meta:
        model = TodoList
        fields = ('id', 'title')


class TodoListDetailSerializer(serializers.ModelSerializer):
    """Get all fields from TodolList"""

    class Meta:
        model = TodoList
        fields = "__all__"


class TodoListCreatSerializer(serializers.ModelSerializer):
    """Create Todolist"""
    created = serializers.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    due_date = serializers.DateField(default=timezone.now().strftime('%Y-%m-%d'))

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'content', 'created', 'due_date', 'category')

