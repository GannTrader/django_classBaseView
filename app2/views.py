from django.shortcuts import render
from .forms import FormBV
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
	form = FormBV
	return render(request, 'app2/form.html', {'form': form})

# def myview(request):
# 	if request.method == 'POST':
# 		form = FormBV(request.POST)
# 		if form.is_valid():
# 			return HttpResponse('success')
# 	else:
# 		form = FormBV(initial = {'key': 'value'})
# 	return render(request, 'formClassBV/form.html', {'form': form})

class myFormView(View):
	form_class = FormBV
	initial = {'key': 'value'}
	template_name = 'app2/form.html'

	def get(self, request):
		form = self.form_class(initial = self.initial)
		return render(request, self.template_name, {'form':form})
	
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():

			#cleaned_data
			return HttpResponse('success')

		return render(request, self.template_name, {'form': form})
			