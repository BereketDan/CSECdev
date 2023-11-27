from django.db import models

# Create your models here.
class Member(models.Model):
  fisrtname = models.CharField(max_length=255)
  ugr = models.CharField(max_length=255)
  sex = models.CharField(max_length=255)
  department  = models.CharField(max_length=255)
  year = models.CharField(max_length=255)
  skill = models.CharField(max_length=255)
  def __str__(self):
        return self.fisrtname


class User_auth(models.Model):
  userName = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  def __str__(self):
        return self.userName

class Event(models.Model):
  eventName = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  hour = models.CharField(max_length=255)
  date = models.CharField(max_length=255)
  def __str__(self):
        return self.eventname


class Feedback(models.Model):
  Telegram_username = models.CharField(max_length=255)
  message = models.CharField(max_length=255)
  messageDate = models.CharField(max_length=255)
  def __str__(self):
        return self.Telegram_username

  