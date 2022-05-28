from django.urls import path
from . import views

urlpatterns = [
    path('review', views.get_drug_review),
    path('review/csv', views.get_drug_review_as_csv),
]