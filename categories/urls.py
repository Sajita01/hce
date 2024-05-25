from django.urls import path
from . import views

urlpatterns= [
    #path('categories/', include('categories.urls')),
    path('', views.category_list, name='category_list'),
]