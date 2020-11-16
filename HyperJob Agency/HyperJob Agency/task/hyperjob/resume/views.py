from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from resume.models import Resume

class ResumeView(View):
    def get(self, request, *arg, **kwargs):
        return render(request, "list.html", {'users': Resume.objects.all})


class NewResumeView(View):
    def post(self, request, *arg, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            Resume.objects.create(description=request.POST['description'], author=request.user)
            return redirect('/home')
        else:
            raise PermissionDenied
