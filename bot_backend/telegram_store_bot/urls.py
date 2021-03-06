from django.contrib import admin
from django.urls import path, include

BASE_API_PATH = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_API_PATH, include('category.urls')),
    path(BASE_API_PATH, include('product.urls')),
    path(BASE_API_PATH, include('customer.urls')),
    path(BASE_API_PATH, include('cart.urls'))
]
