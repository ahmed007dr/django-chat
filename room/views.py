from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Room ,Message

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room_detail(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'room/room_detail.html', {'room': room , 'messages': messages})
