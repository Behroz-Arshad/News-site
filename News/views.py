from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='6f5ab22525134af0a8446e3ff3c06128')
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'News/index.html', context={"mylist": mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="6f5ab22525134af0a8446e3ff3c06128")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'News/BBC.html', context={"mylist": mylist})