from django.db import models
from matplotlib.pyplot import cla

class order(models.Model):


    orderDate=models.DateField(auto_now_add=True)
    orderState=models.IntegerField(default=0)

    sellerAddress=models.CharField(max_length=256,null=False)
    sellerPhone=models.CharField(max_length=256,null=False)
    sellerName=models.CharField(max_length=256,null=False)
    seller_id=models.CharField(max_length=256,null=False)

    buyersAddress=models.CharField(max_length=256,null=False)
    buyersPhone=models.CharField(max_length=256,null=False)
    buyersName=models.CharField(max_length=256,null=False)
    buyers_id=models.CharField(max_length=256,null=False)

class shops(models.Model):

    crdate=models.DateField(auto_now_add=True)
    price=models.CharField(max_length=256,null=False)
    imgUrl=models.CharField(max_length=256,null=False)
    title=models.CharField(max_length=256,null=False)
    content=models.CharField(max_length=256,null=False)
    seller_id=models.CharField(max_length=256,null=False)
