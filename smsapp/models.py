from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=50)


class Plane(models.Model):
    name = models.CharField(max_length=50)


# signals
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


comment_status = [('pending', "Pending"), ('approved', 'Approved')]


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    status = models.CharField(max_length=50, choices=comment_status, default='pending')

    # def __str__(self):
    #     return self.user.username


@receiver(pre_save, sender=Comment)
def print_email(sender, instance, **kwargs):
    print(sender.objects.get(id=instance.id).status)
    print(instance.status)





