from django.urls import path

from posts import views

urlpatterns = [
    path('base_layout/', views.base_layout, name="base-layout"),
    path('', views.index, name="index"),
]
