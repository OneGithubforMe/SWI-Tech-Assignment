from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pharma/', include("pharma.urls")),
    path('drug/', include("drug_review.urls")),
]
