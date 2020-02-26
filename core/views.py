from django.shortcuts import render
from django.http import HttpResponse

from .models import Note

def base(request):
    return HttpResponse("Hello, world.")


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {"notes": notes})


def notes_detail(request, pk):
    notes = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {"notes": note, "pk": pk})

