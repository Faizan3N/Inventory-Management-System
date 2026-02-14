from django.shortcuts import render

# Create your views here.
from .forms import ProductForm
from .models import Product

# CRUD = ['Create', 'Read', 'Update', 'Delete']

def home_view(request):
    return render(request, 'home.html')

