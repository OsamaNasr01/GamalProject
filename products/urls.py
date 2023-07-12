
from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.product, name='product'),
    path('brands/', views.brands, name='brands'),
    path('categories/', views.categories, name='categories'),
    path('product/<slug:slug>/', views.productdetails, name='productdetails'),
]
