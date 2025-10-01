from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse

@login_required
def delete_user(request):
    """
    Allows a logged-in user to delete their account.
    All related data will be cleaned up via signals.
    """
    user = request.user
    user.delete()
    return HttpResponse("Your account and related data have been deleted.")
