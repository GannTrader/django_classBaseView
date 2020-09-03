from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
# Create your views here.
def index(request):
	return render(request, 'app1/index.html')

class contactView(TemplateView):
	template_name = 'app1/contact.html'

class MyView(View):
	def get(self, request):
		return HttpResponse('this is myview class')


class GreetingView(View):
	greeting = 'hello everybody'

	def get(self, request):
		return HttpResponse(self.greeting)

class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"