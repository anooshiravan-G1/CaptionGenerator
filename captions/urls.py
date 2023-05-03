from django.urls import path
from .views import generate_caption, captionAndImageOutput


app_name = 'captions'

urlpatterns = [
    path('', generate_caption, name='generate_caption'),
    path('captionAndImage/<int:pk>/', captionAndImageOutput, name='captionAndImageOutput'),
]
