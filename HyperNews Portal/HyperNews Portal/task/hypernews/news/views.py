import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from datetime import datetime
class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        # return render(request, 'vacancy/menu.html')
        print(HttpResponse("Coming soon"))
        return redirect('/news/')


class NewsView(View):
    def get(self, request, news_id, *args, **kwargs):
        current_news = {}
        with open(settings.NEWS_JSON_PATH) as json_file:
            data = json.load(json_file)
            for i in data:
                if i['link'] == int(news_id):
                    current_news = i
        return render(request, 'news.html', context={'current_news': current_news})


class NewsListView(View):
    def get(self, request, *args, **kwargs):
        news_list = {}
        news_filter = request.GET.get('q', '')
        with open(settings.NEWS_JSON_PATH) as json_file:
            data = json.load(json_file)
            for i in data:
                if news_filter in i['title']:
                    d = i['created'].split()[0]
                    if d not in news_list:
                        news_list[d] = []
                    news_list[d].append(i)
        return render(request, 'news_list.html', context={'news_list': sorted(news_list, reverse=True), 'news_hash': news_list})


class NewsCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create.html')

    def post(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, "r+") as json_file:
            data = json.load(json_file)
            new_value = {"created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                         "text": request.POST.get('text'),
                         "title": request.POST.get('title'),
                         "link": str(round(datetime.timestamp(datetime.now())))}
            data.append(new_value)
            json_file.seek(0)
            json.dump(data, json_file)
        return redirect('/news/')