from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
	context = { 
		'posts': Post.objects.all(),
		'title': 'Main'
	}
	return render(request, 'blog/home.html', context)

def about(request):
	context = { 'title': 'Home' }
	return render(request, 'blog/about.html', context)

