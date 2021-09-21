from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryList

urlpatterns = [
    path('categories', CategoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)