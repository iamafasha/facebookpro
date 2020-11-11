from django import forms

class CreatePostForm(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2' , 'placeholder':'Username / Email'}))
    post_images =  forms.
    