from django.db import models
from django.conf import settings
# Create your models here.
from django.db.models import Q
# do this if want to use User
# default is super user =1
User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(content__icontains=query) |
                  Q(slug__iexact=query)
                  )
        return self.filter(lookup)

        # return self.filter(title__icontains=query)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class BlogPost(models.Model):
    #user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    #image = models.FileField(upload_to='image/', blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.TextField()
    content = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-pk']

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset.filter(title__icontains=query)

    def get_absolute_url(self):
        return f"/blog/blog-detail/{self.slug}"

    def get_edit_url(self):
        # return f"{self.get_absolute_url()}/edit"
        return f"/blog/{self.slug}/update"

    # def get_delete_url(self):
    #    return f"{self.get_absolute_url()}/delete"
