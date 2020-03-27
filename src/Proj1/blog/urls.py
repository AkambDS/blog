from django.urls import path, re_path
from blog.views import (
    home_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_list_view,
    blog_post_create_view,
    blog_post_delete_view,
)


#app_name = 'blog'
urlpatterns = [

    re_path(r'^home/$', home_view, name="home"),
    path('bloglist/', blog_post_list_view, name="list_view"),
    path('blog-new/', blog_post_create_view, name="new_view"),
    path('<str:slug>/update/', blog_post_update_view, name="update_view"),
    path('<str:slug>/delete/', blog_post_delete_view, name="delete_view"),

    # re_path(r'^detail/(?P<id>\d+)/$', blog_post_detail, name="detail"), in regulare exp use this
    # re_path(r'^detail/(?P<slug>\w+)/$', blog_post_detail, name="detail"), in regulare exp use this

    #path('detail/<int:id>/', blog_post_detail, name="detail"),
    path('blog-detail/<str:slug>/', blog_post_detail_view, name="detail"),


]
