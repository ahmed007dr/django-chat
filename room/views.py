from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

def room_detail(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    return render(request, 'room/room_detail.html', {'room': room})
