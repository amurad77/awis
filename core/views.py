from django.shortcuts import render
from news.models import News
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

# Create your views here.

def index(request):
    news = News.objects.all().order_by('-id')[0:4]
    
    context = {
        'news': news
    }
    return render(request, 'index.html', context)






def about(request):
    return render(request, 'about.html')