from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2' , 'placeholder':'Username / Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control mr-sm-2', 'placeholder':'Password'}))

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Last Name'}))
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Username'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control' , 'placeholder':'Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'New Password'}))
    password_again = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'}))

class ProfileForm(forms.Form):
    # first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'First Name'}))
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Last Name'}))
    # user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Username'}))
    # email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control' , 'placeholder':'Email'}))
    profile_picture = forms.ImageField(required=False )
    bio = forms.CharField(label='Bio', max_length=100 ,widget=forms.Textarea())