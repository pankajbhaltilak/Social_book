from . import views
from django.urls import path

urlpatterns = [
    path('portfolio', views.portfolio, name='portfolio'),
]