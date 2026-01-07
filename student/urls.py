from django.urls import path
from .views import (StudentListCreateView, StudentUpdateView, StudentDeleteView)
urlpatterns = [
    path('', StudentListCreateView.as_view() , name='student'),
    path('update/<int:pk>/' , StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/' , StudentDeleteView.as_view(), name='delete'),
]
