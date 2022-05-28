from django.urls import path
from . import views

urlpatterns = [
    path('sales', views.get_pharma_sales),
    path('sales/csv', views.get_pharma_sales_csv),
]