from django.contrib import admin
from .models import ImageCaption

# Register your models here.
@admin.register(ImageCaption)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    # list_filter = ('caption',)
    # search_fields = ('caption',)