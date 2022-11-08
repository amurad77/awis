from django.shortcuts import render
from .models import Projects
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def projects(request):
    projects = Projects.objects.all().order_by('-id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(projects, 7) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'projects': page_obj.object_list,
        'page_obj': page_obj,
    }
    return render(request, 'projects.html', context)