from django.urls import path
from .views import form_view, list_view

urlpatterns = [
    path('', form_view, name='form'),
    path('list/', list_view, name='list'),
]