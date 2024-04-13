from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .forms import *
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
# Create your views here.
def main(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            date = datetime.datetime.now()
            if request.POST['form'] == "NewNote":
                form_notes = Form_for_Notes(request.POST)
                if form_notes.is_valid():
                    text = form_notes.cleaned_data['text']
                    title = form_notes.cleaned_data['title']
                    status = form_notes.cleaned_data['status']
                    w2 = models.Notes()
                    w2.text = text
                    w2.date = date
                    w2.dateoflsu = date
                    w2.title = title
                    w2.status = status
                    w2.executor = request.user.username
                    w2.save()
            else:
                form_notes = Edit_status(request.POST)
                if form_notes.is_valid():
                    prkey = form_notes.cleaned_data['form']
                    status = form_notes.cleaned_data['status']
                    w2 = models.Notes.objects.get(pk = int(prkey))
                    w2.status = status
                    w2.dateoflsu = date
                    w2.save()
        form = Form_for_Notes()
        data = models.Notes.objects.all()
        return render(request,'main.html',{'form' : form,'data' : reversed(data), 'username' : request.user.username})
    else:
        return HttpResponseRedirect("/accounts/login")

def comm(request,num):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form_comms = CommentaryForm(request.POST)
            date = datetime.datetime.now()

            if form_comms.is_valid():
                w2 = models.Commentary()
                w2.nickname = request.user.username
                w2.commentary = form_comms.cleaned_data["commentary"]
                w2.date = date
                w2.pk_note = num
                w2.save()
                return HttpResponseRedirect(request.path_info)
        else:
            form = CommentaryForm()
        data = models.Notes.objects.get(pk = num)
        comm = models.Commentary.objects.filter(pk_note = num)
        return render(request, 'commentary.html', {'data' : data,'form': form, 'comm': reversed(comm),'num' : num})
    else:
        return HttpResponseRedirect("/accounts/login")
