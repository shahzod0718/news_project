from django.urls import path
from .views import news_list,news_detail,homePageView,contactPageView,error404PageView,detailPageView


urlpatterns=[
    path('',homePageView,name='home_page'),
    path('news/',news_list,name='all_news_list'),
    path('news/<slug:news>/',news_detail,name='news_detail_page'),
    path('contact-us/',contactPageView,name='contact_page'),
    path('page-404',error404PageView,name='error404_page'),
    path('detail-page/',detailPageView,name='detail_page'),
]
