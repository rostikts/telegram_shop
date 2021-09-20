from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductList, ProductListByCategory
BASE_PATH = 'products'

urlpatterns = [
    path(f'{BASE_PATH}', ProductList.as_view()),
    path(f'{BASE_PATH}/<int:category>', ProductListByCategory.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)