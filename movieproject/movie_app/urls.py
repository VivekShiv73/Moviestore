from django.urls import path
from . import views
app_name = 'movie_app'

urlpatterns = [

    path('', views.index, name="index"),
    path('movie/<int:movie_id>/', views.detail, name="detail"),
    path('update/<int:movie_id>/', views.update, name="update"),
    path('delete/<int:movie_id>/', views.delete, name="delete"),
]