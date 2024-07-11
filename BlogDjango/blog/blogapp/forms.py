from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserSignup(UserCreationForm):
    class Meta:
        model = User  # Specify the User model
        fields = ['username', 'first_name', 'last_name', 'email']

class postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']

    def __init__(self, *args, **kwargs):
        super(postform, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter post title',
        })
        self.fields['desc'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter post description',
            'rows': 5,
        })
