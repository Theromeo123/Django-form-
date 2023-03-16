from django.shortcuts import render
from Django_Form.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.
#DataFlair #Send Email
def feedback(request):
    sub = forms.Feedback()
    if request.method == 'POST':
        sub = forms.Feedback(request.POST)
        subject = 'Welcome to Rucler Technologies'
        message = 'Good Efforts and Hope you are enjoying your Work and any query to plz visit the site and send main to my email mda663541@gmail.com'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})
