from django import forms
from .models import Post, BlockedList


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author", "pub_date", "change_date")


class BlockedListForm(forms.ModelForm):
    class Meta:
        model = BlockedList
        exclude = ("user_blocking",)
