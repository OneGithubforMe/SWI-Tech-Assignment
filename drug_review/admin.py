from django.contrib import admin
from .models import * 

class DrugReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DrugReview._meta.get_fields()]

admin.site.register(DrugReview, DrugReviewAdmin)