from django.contrib import admin
from .models import *
admin.site.register(Member)# Register your models here.
# 
admin.site.register(User_auth)
admin.site.register(Event)
admin.site.register(Feedback)