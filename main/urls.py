
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    # path('your-path/', views.your_view, name='your_view_url_name')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)