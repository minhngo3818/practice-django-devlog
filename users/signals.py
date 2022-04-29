from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):

    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        # Sending greeting message to new user
        subject = "Welcome to DevSearch"
        message = "We are glad you are here"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )

        # Will happen error that authentication is not allowed
        # "SMTPAuthenticationError at /register/
        # To fix: go to google lesssuccure app and turn on
        # Allow less secure apps : not recommended for deployed website


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        # Make sure add condition to trigger update user profile, or it will cause infinite loop of add user
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


#@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:        # try catch wil prevent deleted used resolve no matching user profile html error
        user = instance.user
        user.delete()
    except:
        pass

    print('Deleting user ...')


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
