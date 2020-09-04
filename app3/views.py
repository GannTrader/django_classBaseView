from django.shortcuts import render, get_object_or_404
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
	# model = Publisher
	# queryset = Publisher.objects.all()
	template_name = 'app3/publisher_detail.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Publisher, id = id_)