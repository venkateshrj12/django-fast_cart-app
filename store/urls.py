from django.urls import path

from store.views import *

app_name = 'store' # Namespace for the store app

urlpatterns = [
    path('', index, name='index'),
]