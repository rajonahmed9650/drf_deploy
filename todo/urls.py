from django.urls import path
from .views import Todo_list_create,Todo_detail


urlpatterns = [
    path('todos/',Todo_list_create,name="todos"),
    path('todos/<int:pk>/',Todo_detail)
]