from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsList.as_view(), name='product-list'),
    path('detail/<int:pk>', views.ProductDetails.as_view(), name="product-details"),
    path('create/', views.ProductCreate.as_view(), name="product-create"),
    path('categories/', views.CategoryList.as_view(), name="category-list"),
    path('categories/<str:category_name>', views.ProductsListByCat.as_view(), name='product-list'),
    path('products/function', views.ProductsFuntion, name="products-function"),
]
