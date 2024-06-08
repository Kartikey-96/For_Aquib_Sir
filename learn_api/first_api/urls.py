from django.urls import path
from .views import ProductView, ProductWithIdView, productReviewSerializer



# urlpatterns = [
#       path('product/', ProductView.as_view(), name='products' ),
#       path('product/<int:id> ', ProductWithIdView.as_view(), name='productsId' ),
# ]


urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list'),
    path('products/<int:customerId>/', ProductWithIdView.as_view(), name='product-detail'),
      path('products/<int:productId>/review', productReviewSerializer.as_view(), name='product-detail'),
]
