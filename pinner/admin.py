from django.contrib import admin
from .models import SendMessage, User, Profile, Passion
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Passion)
admin.site.register(SendMessage)

