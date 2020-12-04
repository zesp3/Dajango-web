import json
from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
    
    article1 = {
        "title": "Pierwszy artykuł",
        "date": "2020-08-12",
        "source": "facebook",
        "cont_art": "To jest treść artykułu 1"
    }


    article2 = {
        "title": "Drugi artykuł",
        "date": "2010-01-14",
        "source": "twitter",
        "cont_art": "To jest treść artykułu 2"
    }


    json_string1 = json.dumps(article1)
    json_string2 = json.dumps(article2)
    
    context = {}
    list_of_articles = []
    list_of_articles.append(json_string1)
    list_of_articles.append(json_string2)
    list_of_articles.append(json_string1)
    list_of_articles.append(json_string2)
    list_of_articles.append(json_string1)
    list_of_articles.append(json_string2)
    list_of_articles.append(json_string1)
    list_of_articles.append(json_string2)
    list_of_articles.append(json_string1)
    list_of_articles.append(json_string2)   
    context['list_of_articles'] = list_of_articles
    return render(request, 'index.html', context)
    
def culture(request):
    return render(request, 'culture.html')

def info(request):
    return render(request, 'info.html')

def services(request):
    return render(request, 'services.html')

def transport(request):
    return render(request, 'transport.html')