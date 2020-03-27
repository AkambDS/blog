from django.urls import path
from pages.views import home_view

urlpatterns = [
    
    path('pages/', home_view, name="pages"),
]