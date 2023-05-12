from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .model import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'