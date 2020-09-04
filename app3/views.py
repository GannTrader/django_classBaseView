from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book

class PublisherList(ListView):
    model = Publisher
    # queryset = Publisher.objects.all() -- hoac khai bao nhu tren deu duoc
    # dung queryset thi minh co the filter hoac lam gi cung duoc chu khai bao 
    # moi model thoi thi khong lam gi duoc
    context_object_name = 'my_favorite_publishers'
    template_name = 'app3/publisher.html'

class PublisherDetail(DetailView):
	model = Publisher
	template_name = 'app3/publisher_detail.html'
	# queryset = Publisher.objects.all()

	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
		context['book_list'] = Book.objects.all()
		return context
