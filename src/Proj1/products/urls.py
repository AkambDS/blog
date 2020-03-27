from django.urls import path
from products.views import (
    product_detail_view, 
    product_create_view,
    product_update_view,
    product_lookup_view, 
    product_delete_view,
    product_list_view
)


app_name= 'products'
urlpatterns = [
    
    path('', product_detail_view, name="product_det"),
    path('create/', product_create_view, name="product_create"),
    path('update/', product_update_view, name="product_update"),
    path('search/<int:id>/', product_lookup_view, name="product_search"),
    path('<int:id>/del/', product_delete_view, name="product_del"),
    path('prodlist/', product_list_view, name="product_list"),


]