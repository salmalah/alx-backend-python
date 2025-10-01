from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Message

@login_required
def delete_user(request):
    """
    Allows a logged-in user to delete their account.
    All related data will be cleaned up via signals.
    """
    user = request.user
    user.delete()
    return HttpResponse("Your account and related data have been deleted.")

@login_required
def user_messages(request):
    """
    Display all messages sent by the logged-in user,
    including threaded replies, efficiently.
    """
    messages = Message.objects.filter(sender=request.user).select_related('receiver').prefetch_related('replies')

    # Recursive function to get all replies in threaded format
    def get_thread(message):
        thread = []
        for reply in message.replies.all().select_related('sender', 'receiver').prefetch_related('replies'):
            thread.append(reply)
            thread.extend(get_thread(reply))
        return thread

    threaded_messages = []
    for msg in messages:
        threaded_messages.append({
            'message': msg,
            'thread': get_thread(msg)
        })

    return render(request, 'messaging/user_messages.html', {'threaded_messages': threaded_messages})

@login_required
def unread_inbox(request):
    """
    Display only unread messages for the logged-in user.
    Optimized with .only() via custom manager.
    """
    unread_messages = Message.unread.unread_for_user(request.user)
    return render(request, 'messaging/unread_inbox.html', {'messages': unread_messages})
