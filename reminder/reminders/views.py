#coding: utf-8
from django.shortcuts import render
from note.models import Reminder, Group
from profiles.models import Profile
from reminders.forms import CreateGroup
from django.shortcuts import redirect
from django.contrib import messages
from profiles import views

def add_group(request):
    profile = Profile.objects.all()
    if request.POST:
        create = Group.objects.create(name=request.GET.get('message'))
        for i in request.POST.getlist('browser'):
            create.user.add(int(i))
        messages.success(request, 'Спасибо вы создали группу')
        tr = create.id
        return redirect('reminders:reminders', group_idi=int(create.id))
    return render(request, 'reminder/add_group.html', {'profile': profile})


def add_reminders(request, group_id):
    create = Reminder.objects.create(name=request.GET.get('name'))
    create.group = Group.objects.get(pk=1)
    return render(request, 'reminder/add_reminder.html', {})


def reminders_page(request, group_idi):
    return render(request, 'reminder/reminder.html', {})
