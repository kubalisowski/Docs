from django.shortcuts import render
from . import forms  ### might be also from basicapp import forms

def index(request):  ### just for index page
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()   ### Importing previously created class of form from form.py; empty instance of class

    if request.method == 'POST':
        form = forms.FormName(request.POST)   ### form object filled with data from sent form (POST request)

        if form.is_valid():   ### boolean value
            print('VALIDATION OK!')
            ### Printing data grabbed from data sent via form --> .cleaned_data[] method;
            print(form.cleaned_data['name']) ## 'name' variable declared in forms.py
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])


    return render(request, 'basicapp/form_page.html', {'form' : form})

