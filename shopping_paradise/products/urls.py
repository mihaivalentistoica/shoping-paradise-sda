from django.urls import path, include
from rest_framework import routers

from .views import (CategoryList, CategoryDetails, CategoryUpdate, CategoryDelete, CategoryCreate, ProductsList,
                    ProductDetails, ProductUpdate, ProductDelete, ProductCreate, coupon_view, thank_you, session_view,
                    ProductViewSet, CategoryViewSet)

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

categories_urlpatterns = [
    path('', CategoryList.as_view(), name="category-list"),
    path('detail/<int:pk>', CategoryDetails.as_view(), name="category-detail"),
    path('update/<int:pk>', CategoryUpdate.as_view(), name="category-update"),
    path('delete/<int:pk>', CategoryDelete.as_view(), name="category-delete"),
    path('create/', CategoryCreate.as_view(), name="category-create"),
]

product_urlpatterns = [
    path('', ProductsList.as_view(), name='product-list'),
    path('detail/<int:pk>/', ProductDetails.as_view(), name="product-details"),
    path('update/<int:pk>/', ProductUpdate.as_view(), name="product-update"),
    path('delete/<int:pk>/', ProductDelete.as_view(), name="product-delete"),
    path('create/', ProductCreate.as_view(), name="product-create"),
]

coupon_urlpatterns = [
    path('create', coupon_view, name="create-coupon"),
    path('thankyou', thank_you, name="thank-you"),
]

urlpatterns = [
    path('', include(product_urlpatterns)),
    path('categories/', include(categories_urlpatterns)),
    path('coupon/', include(coupon_urlpatterns)),
    path('views/', session_view, name="counter"),
    path('rest-api/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-api/', include(router.urls)),
]
