from django.shortcuts import render
from django.views.generic import ListView
from .models import post
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_protect


# Create your views here.
# @method_decorator(name='dispatch', decorator=csrf_protect)
class HomePageView(ListView):
    model = post
    template_name = "home.html"