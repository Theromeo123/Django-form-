from django.http import HttpResponseRedirect
from django.shortcuts import render

from Review.forms import ReviewForm

# Create your views here.
def review(request):
    form = ReviewForm()
    if (request.method == 'POST'):
          form = ReviewForm(request.POST)
    
    if form.is_valid():
           return HttpResponseRedirect("/thank-you")   

    return render(request,"reviews/review.html", {
        "form": form
    })


def thankyou(request):
    return render(request,"reviews/thanks.html")