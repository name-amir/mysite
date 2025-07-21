from django.shortcuts import render
from website.forms import NameForm,ConatactForm,NewsletterForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.



def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ConatactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            messages.add_message(request,messages.SUCCESS,'your ticket submited seuccessfuly')
            if name:  # فقط اگر نامی وارد شده باشد
                form.cleaned_data['name'] = 'Anonymous'
            form.save()


        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited seuccessfuly')
    form = ConatactForm()
    return render(request, 'website/contact.html',{'form':form})

def test_view(request):
    # context = {'name': 'Amir','lastname':'Moradi'}
    # return render(request, 'website/test.html', context)
    if request.method == 'POST':
        form = ConatactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ConatactForm()
    return render(request, 'test.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')

