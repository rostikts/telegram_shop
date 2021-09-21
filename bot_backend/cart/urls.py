from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CartView, CartItemsView, CartDetailView, CartItemDetails, CompleteActiveChatView

urlpatterns = [
    path('cart', CartView.as_view()),
    path('cart/<int:cart_id>', CartDetailView.as_view()),
    path('cart/<int:cart_id>/complete', CompleteActiveChatView.as_view()),
    path('cart/<int:cart_id>/items', CartItemsView.as_view()),
    path('cart/<int:cart_id>/items/<int:item_id>', CartItemDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)