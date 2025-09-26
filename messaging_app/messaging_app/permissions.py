from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Only allow users to access their own messages.
    Assumes the object has a 'user' field.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsParticipant(permissions.BasePermission):
    """
    Only participants of a conversation can access it.
    Assumes the object has a 'participants' field (ManyToManyField).
    """
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()
