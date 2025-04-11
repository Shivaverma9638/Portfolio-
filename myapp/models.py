from django.db import models

# Create your models here.
# class enquiry(models.Model):
#    id=models.IntegerField(primary_key=True,auto_created=True)
#    name=models.CharField(max_length=225)
#    gender=models.CharField(max_length=10)
#    address=models.CharField(max_length=500)
#    contactno=models.IntegerField(max_length=15)
#    emailaddress=models.EmailField(max_length=100)

class AdminLogin(models.Model):
   userid=models.CharField(max_length=50)
   password=models.CharField(max_length=50)