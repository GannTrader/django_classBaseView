from django.urls import path
from .import views 

urlpatterns = [
    # path('', views.index),
    # path('myview/', views.myview, name = 'myview'),
    path('myFormView/', views.myFormView.as_view(), name = 'myFormView'),
]