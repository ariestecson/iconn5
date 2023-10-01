from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.decorators import login_required
from .models import Lecture
# Create your views here.
@login_required(login_url='/iconn/login/')
def index(request):
    lectures = Lecture.objects.all()
    context = {
        'lectures': lectures
    }
    return render(request, 'myapp/index.html', context)

@xframe_options_sameorigin
@login_required(login_url='/accounts/login/')
def lecture_view(request, pk):
    lecture = Lecture.objects.get(pk=pk)

    context = {
        'lecture': lecture
    }

    return render(request, 'myapp/lecture_details.html', context)
