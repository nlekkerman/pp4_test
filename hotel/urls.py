from . import views
from django.urls import path

urlpatterns = [
    path('hotel/', views.hello_blog, name='hotel'),
]