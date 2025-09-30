from django.shortcuts import render,get_object_or_404
from .models import News,Category
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

def news_list(request):
    news_list=News.published.all()
    context={
        'news_list':news_list,
    }

    return render(request,'news/news_list.html',context)

def news_detail(request,news):
    news=get_object_or_404(News,slug=news,status=News.Status.Published)
    context={
        'news':news
    }
    return render(request,'news/news_detail.html',context)

def homePageView(request):
    categories=Category.objects.all()
    news_one=News.published.order_by('-publish_time')[:1]
    news_two=News.published.order_by('-publish_time')[1:2]
    news_list=News.published.all().order_by('-publish_time')[2:6]

    local_one=News.published.filter(category__name='mahalliy').order_by('-publish_time')[:1]
    local_news=News.published.all().filter(category__name='mahalliy').order_by('-publish_time')[1:6]
    
    sport_one=News.published.filter(category__name='sport').order_by('-publish_time')[:1]
    sport_news=News.published.all().filter(category__name='sport').order_by('-publish_time')[1:6]
    

    xorij_one=News.published.filter(category__name='xorij').order_by('-publish_time')[:1]
    xorij_news=News.published.all().filter(category__name='xorij').order_by('-publish_time')[1:6]


    techno_one=News.published.filter(category__name='texnologiya').order_by('-publish_time')[:1]
    techno_news=News.published.all().filter(category__name='texnologiya').order_by('-publish_time')[1:6]

    shou_biznes=News.published.filter(category__name='shouBiznes').order_by('-publish_time')[:2]

    context={
        'news_list':news_list,
        'news_one':news_one,
        'news_two':news_two,
        'categories':categories,
        'local_one':local_one,
        'local_news':local_news,
        'sport_one':sport_one,
        'sport_news':sport_news,
        'xorij_one':xorij_one,
        'xorij_news':xorij_news,
        "techno_one":techno_one,
        'techno_news':techno_news,
        'shou_biznes':shou_biznes,
    
    }
    return render(request,'news/home.html',context)


def contactPageView(request):
    
    form =ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("biz bilan boglanganingiz uchun raxmat")
    context = {
        'form':form
    }
    return render(request,'news/contact.html',context)


def error404PageView(request):
    context={

    }
    return render(request,'news/404.html',context)






def detailPageView(request,):
    
    context={
    
    }
    return render(request,'news/detail-page.html',context)







