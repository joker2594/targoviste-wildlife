from django import forms
from wildlife.models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('description', 'picture', )