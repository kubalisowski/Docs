from django.shortcuts import render
from . import forms  ### might be also from basicapp import forms
from .models import Users

def index(request):  ### just for index page
    return render(request, 'basicapp/index.html')

def theform(request):
    form = forms.ModelForm()

    if request.method == 'POST':
        form = forms.ModelForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            email = form.cleaned_data['email']
            print(email)
            ### https://stackoverflow.com/questions/40224136/django-save-form-data-to-database
            user = Users(name=name, email=email)
            user.save()


    return render(request, 'basicapp/form_page.html', {'form' : form})