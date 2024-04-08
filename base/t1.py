    room_messages = room.message_set.all()
    context = {'room': room, 'room_messages': room_messages}
    return render(request, 'base/room.html', context)