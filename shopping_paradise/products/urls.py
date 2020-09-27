from django.urls import path, include
from . import views

categories_urlpatterns = [
    path('', views.CategoryList.as_view(), name="category-list"),
    path('detail/<int:pk>', views.CategoryDetails.as_view(), name="category-detail"),
    path('update/<int:pk>', views.CategoryUpdate.as_view(), name="category-update"),
    path('delete/<int:pk>', views.CategoryDelete.as_view(), name="category-delete"),
    path('create/', views.CategoryCreate.as_view(), name="category-create"),
]

product_urlpatterns = [
    path('', views.ProductsList.as_view(), name='product-list'),
    path('detail/<int:pk>/', views.ProductDetails.as_view(), name="product-details"),
    path('update/<int:pk>/', views.ProductUpdate.as_view(), name="product-update"),
    path('delete/<int:pk>/', views.ProductDelete.as_view(), name="product-delete"),
    path('create/', views.ProductCreate.as_view(), name="product-create"),
]

coupon_urlpatterns = [
    path('create', views.coupon_view, name="create-coupon"),
    path('thankyou', views.thank_you, name="thank-you"),
]

urlpatterns = [
    path('', include(product_urlpatterns)),
    path('categories/', include(categories_urlpatterns)),
    path('coupon/', include(coupon_urlpatterns)),
    path('views/', views.session_view),
]
