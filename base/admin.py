from django.contrib import admin
from .models import Rooms,Topic,Message,User
# Register your models here.

admin.site.register(Rooms)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(User)