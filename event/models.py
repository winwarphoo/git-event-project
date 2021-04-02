from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class EventCreator(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["user", "date_of_birth"]
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("eventcreator-detail", args=[str(self.id)])

class Event(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(EventCreator, on_delete=models.CASCADE, blank=True)
    about = models.TextField(help_text="Enter about of event")
    date_of_start = models.DateField(null=True, blank=True)
    date_of_end = models.DateField('ended', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id', 'name', 'date_of_start']
    
    def get_absolute_url(self):
        return reverse("event-detail", args=[str(self.id)])

class EventAttendence(models.Model):
    profile = models.ImageField(upload_to='images/', default='defo')
    name = models.CharField(max_length=1000, help_text="Enter your Name")
    email = models.EmailField(max_length=70,blank=True,unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=12)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ["name"]

