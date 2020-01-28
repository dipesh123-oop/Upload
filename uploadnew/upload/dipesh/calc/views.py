# Create your views here.
from django.shortcuts import render
from .models import File
from .forms import FileForm


def showfile(request):

    lastfile = File.objects.last()

    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context= {'lastfile':lastfile,
              'form':form
              }

    return render(request, 'files.html', context)
