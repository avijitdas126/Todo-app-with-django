from django.contrib import admin
from .models import User_Model,Todo
# Register your models here.
@admin.register(User_Model,Todo)
class showdb(admin.ModelAdmin):
    pass