from django.urls import path
from .views import ProductDetail, product
from . import views
app_name = 'product'
urlpatterns = [
    path('detail/<int:id>', ProductDetail.as_view(), name='detail'),
    path('', views.product, name='product'),
]
