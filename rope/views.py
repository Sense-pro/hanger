from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect

# Create your views here.

class Index(View):
	def get(self, request, *args, **kwargs):
		return	render(request, 'index.html', {})