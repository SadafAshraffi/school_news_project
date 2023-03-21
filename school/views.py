from django.shortcuts import render
from school.models import News






def index(request):
    news_list = News.objects.all()
    context_dict = {}
    context_dict['news'] = news_list
    return render(request, 'school/index.html', context=context_dict)


