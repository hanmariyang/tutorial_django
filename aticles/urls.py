from django.urls import path
from aticles import views


app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>/', views.dinner),
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
]
