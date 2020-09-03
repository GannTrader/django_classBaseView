from django.urls import path
from django.views.generic import TemplateView
from .import views

urlpatterns = [
	# c1 - viet binh thuong qua view
	path('index/', views.index),
	# c2 - dung templateview ngan gon, nhanh
    path('about/', TemplateView.as_view(template_name = 'app1/about.html')),
    # c3 - viet thong qua class
    path('contact/', views.contactView.as_view()),

    # c4 - viet dang View
    path('myview/', views.MyView.as_view()),

    path('greeting/', views.GreetingView.as_view()),
    #overide cai greeting o ben trang views.py
    # path('greeting/', views.GreetingView.as_view(greeting = 'hello world'))
    #overide bang subclass o ben trang view
    # path('greeting/', views.MorningGreetingView.as_view())

]