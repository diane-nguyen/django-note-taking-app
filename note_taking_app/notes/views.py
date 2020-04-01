from django.shortcuts import render
from django.http import HttpResponseRedirect
# import eachNote class from models file within 
# the same directory
from .models import eachNote

# create view
# connect to specific url from url.py
def notesView(request):
    all_notes = eachNote.objects.all()
    return render(request,'notes.html',
        {'view_all': all_notes})

def addNote(request):
    new_Note = eachNote(content = request.POST['content'])
    new_Note.save()
    return HttpResponseRedirect('/notes/')

def deleteNote(request, note_id):
    note_to_delete = eachNote.objects.get(id=note_id)
    note_to_delete.delete()
    return HttpResponseRedirect('/notes/')
