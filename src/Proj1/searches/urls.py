from django.urls import path, re_path
from searches.views import (
    search_view,
)


#app_name = 'blog'
urlpatterns = [


    path('', search_view, name="search_view"),

]
