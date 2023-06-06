from django.contrib import admin
from websiteservices.models import Feedback

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('customer_name','email_address','suggestion')
    
admin.site.register(Feedback,ServiceAdmin)
