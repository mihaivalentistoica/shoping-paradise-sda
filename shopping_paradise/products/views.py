from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product, Category
from .form import CouponForm


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


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'update_product.html'
    fields = "__all__"

    def get_success_url(self):
        return reverse('product-details', kwargs={'pk': self.kwargs['pk']})


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product-list')


class ProductsList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['price']


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryDetails(DetailView):
    model = Category
    template_name = 'category_details.html'
    context_object_name = 'category'


class CategoryCreate(CreateView):
    model = Category
    template_name = 'category_add.html'
    fields = "__all__"
    success_url = reverse_lazy('category-list')


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'category_update.html'
    fields = "__all__"

    def get_success_url(self):
        return reverse('category-detail', kwargs={'pk': self.kwargs['pk']})


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category-list')


def ProductsFuntion(request):
    list_of_products = Product.objects.all().order_by('price')
    print(list_of_products)
    context = {
        'products': list_of_products
    }
    return render(request, 'products_function.html', context)


def coupon_view(request):
    if request.method == 'GET':
        form = CouponForm()
        return render(request, 'coupon_create.html', {'form': form})
    elif request.method == "POST":
        form = CouponForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/products/coupon/thankyou")
        else:
            return render(request, 'coupon_create.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')


def session_view(request):
    count = request.session.get('views', 0)
    count += 1
    request.session['views'] = count
    print(dir(request.session))
    print(request.user)
    return render(request, 'views_page.html', {'views': count})
