from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CustomerList

urlpatterns = [
    path('customers', CustomerList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)