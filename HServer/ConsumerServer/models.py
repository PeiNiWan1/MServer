import email
from django.db import models

# Create your models here.
class userS(models.Model):
    user_name=models.CharField(max_length=256,null=False)
    nick=models.CharField(max_length=256,null=False)
    phone_number=models.CharField(max_length=256,null=False)
    email=models.CharField(max_length=256,null=True)
    password=models.CharField(max_length=256,null=False)

    department=models.CharField(max_length=256,null=True)
    specialty=models.CharField(max_length=256,null=True)
    #权限
    puissance=models.IntegerField(default=1 )
    register_date=models.DateField(auto_now_add=True)
class userP(models.Model):
    userP_id=models.IntegerField(primary_key=True)
    img=models.CharField(max_length=256,null=True)
    buy=models.CharField(max_length=256,null=True)
    sellout=models.CharField(max_length=256,null=True)
    address=models.CharField(max_length=256,null=True)
