from django.db import models

# Create your models here.
class Feedback(models.Model):
    customer_name = models.CharField(max_length=50, null=False)
    email_address = models.EmailField(max_length=200, null=False)
    suggestion = models.TextField()