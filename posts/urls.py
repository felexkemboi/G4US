
from django.urls import path
from . import views
from . views import PostViewSet

urlpatterns = [
  path('',                        views.posts,      name = 'posts'),
  path('home/',                   views.home,       name = 'home'),
  path('new/',                    views.new_post,   name = 'new_post'),
  path('<int:pk>/edit/',          views.edit,       name = 'edit'),
  path('<int:pk>/delete/',        views.delete,     name = 'delete'),
  path('<int:pk>/',               views.detail,     name = 'detail'),
  path('<int:pk>/comment',        views.comment,    name = 'comment'),
  path('<int:pk>/comment/remove', views.remove,    name = 'remove'),
  path('api/', PostViewSet.as_view({'get': 'list'}),             name="songs-all")


]