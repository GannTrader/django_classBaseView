from django.urls import path, include
from .import views

urlpatterns = [
    path('publishers/', views.PublisherList.as_view()),
    path('PublisherDetail/<int:id>', views.PublisherDetail.as_view(), name = 'PublisherDetail'),
]