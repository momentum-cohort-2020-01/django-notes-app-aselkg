from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Note
from .forms import NoteForm

def base(request):
    return render(request, 'base.html')


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {"notes": notes})


def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/note_detail.html', {"note": note, "pk": pk})

def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        # if form.is_valid():
        note = form.save()
        return redirect('note_detail', note.pk)
    else:
        form = NoteForm()

    return render(request, 'core/note_edit.html', {"form": form})


def edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        # if form.is_valid():
        note = form.save(commit=False)
        note = form.save()
        return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/note_edit.html', {'form': form})