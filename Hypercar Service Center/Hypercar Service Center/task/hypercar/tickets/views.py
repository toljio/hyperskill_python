from django.views import View
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect

my_menu = [
    {
        "desc": "Change oil",
        "link": "/get_ticket/change_oil",
    },
    {
        "desc": "Inflate tires",
        "link": "/get_ticket/inflate_tires"
    },
    {
        "desc": "Get diagnostic test",
        "link": "/get_ticket/diagnostic",
           }
]
line_of_cars = {
    "change_oil": [],
    "inflate_tires": [],
    "diagnostic": [],
}
ticket_number = 0
next_id = 0
class WelcomeView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *arg, **kwargs):
        return render(request, 'menu.html', context={'my_menu': my_menu})

class ServeView(View):
    def get(self, request, serve_action, *arg, **kwargs):
        if serve_action not in line_of_cars:
            raise Http404
        if serve_action == "change_oil":
            minutes = 2 * len(line_of_cars["change_oil"])
        elif serve_action == "inflate_tires":
            minutes = 2 * len(line_of_cars["change_oil"]) + 5 * len(line_of_cars["inflate_tires"])
        elif serve_action == "diagnostic":
            minutes = 2 * len(line_of_cars["change_oil"]) + 5 * len(line_of_cars["inflate_tires"]) + 30 * len(line_of_cars["diagnostic"])
        global ticket_number
        ticket_number += 1
        line_of_cars[serve_action].append(ticket_number)
        return render(request, 'get_ticket/content.html', context={'ticket_number': ticket_number, 'minutes': minutes})

class ProcessingView(View):
    def get(self, request, *arg, **kwargs):
        return render(request, 'operator_menu.html', context={'change_oil': len(line_of_cars["change_oil"]), 'inflate_tires': len(line_of_cars["inflate_tires"]), 'diagnostic': len(line_of_cars["diagnostic"])})

    def post(self, request, *args, **kwargs):
        global next_id
        if len(line_of_cars["change_oil"]) > 0:
            next_id = line_of_cars["change_oil"].pop(0)
        elif len(line_of_cars["inflate_tires"]) > 0:
            next_id = line_of_cars["inflate_tires"].pop(0)
        elif len(line_of_cars["diagnostic"]) > 0:
            next_id = line_of_cars["diagnostic"].pop(0)
        else:
            next_id = 0
        return redirect('/next')

class NextView(View):
    def get(self, request, *arg, **kwargs):
        if next_id > 0:
            html = f"<div>Next ticket #{next_id}</div>"
        else:
            html = "<div>Waiting for the next client</div>"
        return HttpResponse(html)
