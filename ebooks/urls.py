from django.urls import path
from . import views
from posts import views as posts_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('',                 views.upload,     name = 'upload'),
  path('<int:pk>/',       views.detail,     name = 'ebook-detail'),
  path('<int:pk>/edit/',  views.edit,      name ='ebook-edit'),   
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)