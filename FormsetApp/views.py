from django.shortcuts import render, redirect
from .forms import BookFormset
from .models import Book

def create_book_normal(request):
    template_name = 'create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name1 = form.cleaned_data.get('name')
                # save book instance
                if name1:
                    Book(name=name1).save()
                    print("1 record created")
            # once all books are saved, redirect to book list view
          #  return redirect('book_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })