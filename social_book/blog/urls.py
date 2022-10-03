from . import views
from django.urls import path

urlpatterns = [
    path('bloghome', views.PostList.as_view(), name='bloghome'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]