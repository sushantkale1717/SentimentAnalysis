from django.contrib import admin
from managerestaurants.models import Restaurants

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','content','timeStamp')
    
admin.site.register(Restaurants, ServiceAdmin)