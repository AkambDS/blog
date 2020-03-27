from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required

# USING Raw form


# def blog_post_create_view(request):
#   qs = BlogPost.objects.all()
#  form = BlogPostForm(request.POST or None)
# if form.is_valid():
# print(form.cleaned_data)
#title= form.cleaned_data['title']
#obj = BlogPost.objects.Create(title=title)
# obj.save
# obj2=othermodel.
# if u have fields updating in multiple tables then grab individual data
#    obj = BlogPost.objects.create(**form.cleaned_data)  # unpack the data
#   form = BlogPostForm()
# template_name = 'blog/blog_post_create.html'  # or form.html pass directly
#context = {'form': form}
# return render(request, template_name, context)

# using modal form
@login_required
def blog_post_create_view(request):
    #qs = BlogPostModelForm.objects.all()
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        #title= form.cleaned_data['title']
        #obj = BlogPost.objects.Create(title=title)
        # obj.save
        # obj2=othermodel.
        # if u have fields updating in multiple tables then grab individual data
        # obj = BlogPost.objects.create(**form.cleaned_data)  # unpack the data
        obj = form.save()
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'blog/blog_post_create.html'  # or form.html pass directly
    context = {'form': form}
    return render(request, template_name, context)


# def blog_post_create_view(request):
 #   qs = BlogPost.objects.all()
#    form = BlogPostForm(request.POST or None)
 #   if form.is_valid():
    # print(form.cleaned_data)
    #title= form.cleaned_data['title']
    #obj = BlogPost.objects.Create(title=title)
    # obj.save
    # obj2=othermodel.
    # if u have fields updating in multiple tables then grab individual data
  #      obj = BlogPost.objects.create(**form.cleaned_data)  # unpack the data
  #      form = BlogPostForm()
  #  template_name = 'blog/blog_post_create.html'  # or form.html pass directly
  #  context = {'form': form}
  #  return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, 'title': f'Update{obj.title}'}
    return render(request, template_name, context)


# @staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_detete.html'
    if request.method == "POST":
        obj.delete()
        # / means root and grab url from urls.py file
        return redirect('/blog/bloglist')
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    # qs = BlogPost.objects.filter(title__icontains="hello')
    template_name = 'blog/blog_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


# def blog_post_detail(request, slug):
    #obj = get_object_or_404(BlogPost, id=id)
 #   obj = get_object_or_404(BlogPost, slug=slug)
    # queryset = BlogPost.objects.filter(slug=slug)  # returns multiple set /list
    # if queryset.count() == 0:
   #     raise Http404

   # obj = queryset.first()
 #   template_name = 'blog/blog_post_detail.html'
 #   context = {"object": obj}
 #   return render(request, template_name, context)

# Create your views here.


def home_view(request):
    my_title = "Shreya Blog"
    context = {'title': my_title}
    return render(request, "blog/blog_list.html", context)
