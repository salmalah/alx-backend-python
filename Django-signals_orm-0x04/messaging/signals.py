from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.db.models.signals import post_delete
from django.contrib.auth.models import User


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_message = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return

    if old_message.content != instance.content:
        # Mark as edited
        instance.edited = True
        # Save old content in MessageHistory
        MessageHistory.objects.create(
            message=instance,
            old_content=old_message.content,
            edited_by=instance.sender  # assuming sender edited the message
        )

@receiver(post_delete, sender=User)
def delete_related_data(sender, instance, **kwargs):
    """
    Automatically deletes all messages, notifications, and message histories
    related to a user when the user account is deleted.
    """
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    
    Notification.objects.filter(user=instance).delete()
    
    MessageHistory.objects.filter(edited_by=instance).delete()
