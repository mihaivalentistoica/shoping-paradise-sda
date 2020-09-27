from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView

from .models import Product, Category


class ProductsListByCat(View):
    def get(self, request, category_name):
        products = Product.objects.filter(category__name=category_name)
        return HttpResponse(products)


class ProductDetails(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"


class ProductCreate(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductsList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['name']


class CategoryList(View):
    def get(self, request):
        categoryes = Category.objects.all()
        return HttpResponse(categoryes)


def ProductsFuntion(request):
    list_of_products = Product.objects.all().order_by('price')
    print(list_of_products)
    context = {
        'products': list_of_products
    }
    return render(request, 'products_function.html', context)
