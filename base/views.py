from django.shortcuts import render
from .models import Room

rooms = [
    {'id': 1, 'name': 'room 1'},
    {'id': 2, 'name': 'room 2'},
    {'id': 3, 'name': 'room 3'},
]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)