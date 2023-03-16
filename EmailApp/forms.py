from django import forms

class Feedback(forms.Form):
    Email = forms.EmailField()
    
    def __str__(self):
        return self.Email