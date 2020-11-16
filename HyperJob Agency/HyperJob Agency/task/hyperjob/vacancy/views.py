from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Vacancy
from django.core.exceptions import PermissionDenied

class VacancyView(View):
    def get(self, request, *arg, **kwargs):
        return render(request, "list.html", {'users': Vacancy.objects.all})


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            Vacancy.objects.create(description=request.POST['description'], author=request.user)
            return redirect('/home')
        else:
            raise PermissionDenied
