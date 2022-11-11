from django.shortcuts import render
from news.models import News
from core.models import Statitics, Partners
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import InvolvedForm
from django.contrib import messages


# Create your views here.

def index(request):
    partners = Partners.objects.all().order_by('-id')

    news = News.objects.all().order_by('-id')[0:4]
    
    context = {
        'news': news,
        'partners': partners,
        'navbar': 'home_page'

    }
    return render(request, 'index.html', context)






def about(request):
    partners = Partners.objects.all().order_by('-id')
    statitics = Statitics.objects.all()

    context = {
        'partners': partners,
        'statitics': statitics,
        'navbar': 'about'
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
            # return HttpResponseRedirect('/opportunities/')
        else:
            # form = ContactForm()
            # submitted = True
            print('Form is invalid')

    context = {
        'form': form,
        'navbar': 'opportunities'
    }
    return render(request, 'opportunities.html', context)