from django import forms
from .models import BlogPost


# class BlogPostForm(forms.Form):
#    title = forms.CharField()
#    slug = forms.SlugField()
#    content = forms.CharField(widget=forms.Textarea)

# add some validation for form fields
#   def clean_title(self, *args, **kwargs):
#        title = self.cleaned_data.get('title')
#        print(title)
#        if title.endswith("hello"):
#            raise forms.ValidationError("deekh key bhai")
#        return title
# modal form


class BlogPostModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(  # or chnage in model
        attrs={
            'class': 'form-control',
            # 'div class': 'col-sm-8',
        }
    ))
    slug = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }

    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }

    ))

    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'image']

    # add some validation for form fields
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError(
                "title exist from mdal form validation")
        return title
