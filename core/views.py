from django.shortcuts import render
from news.models import News
from core.models import Statitics
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import InvolvedForm
from django.contrib import messages


# Create your views here.

def index(request):
    news = News.objects.all().order_by('-id')[0:4]
    
    context = {
        'news': news
    }
    return render(request, 'index.html', context)






def about(request):
    statitics = Statitics.objects.all()

    context = {
        'statitics': statitics
    }
    return render(request, 'about.html', context)

def opportunities(request):
    form = InvolvedForm()
    if request.method == 'POST':
        contact_data = request.POST
        form = InvolvedForm(data=contact_data)
        # submitted = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your interest! We will reply to you within 2-3 working days.')
            print('Form save')
            # submitted = True
            return HttpResponseRedirect('/opportunities/')
        else:
            # form = ContactForm()
            # submitted = True
            print('Form is invalid')

    context = {
        'form': form
    }
    return render(request, 'opportunities.html', context)