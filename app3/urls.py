from django.urls import path, include
from .import views

urlpatterns = [
    path('publishers/', views.PublisherList.as_view()),
    path('PublisherDetail/<int:pk>', views.PublisherDetail.as_view(), name = 'PublisherDetail'),
]