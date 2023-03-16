from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="User Name", max_length=100)
    user_pwd = forms.CharField(label="Password",max_length=10, widget = forms.PasswordInput())

