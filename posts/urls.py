
from django.urls import path
from . import views

urlpatterns = [
  path('',                 views.home,        name= 'list'),
  path('new/',             views.new,         name= 'new'),
  path('<int:pk>/edit/',   views.edit,        name = 'edit'),
  path('<int:pk>/delete/', views.delete,      name = 'delete'),
  path('<int:pk>/',        views.detail ,     name = 'detail'),
]