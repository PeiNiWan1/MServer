from dataclasses import dataclass
import json
from re import I
import time
from tkinter import W
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import get
from HServer import settings
from app.models import order, shops

def createShop(request):

    if request.session.get("user_id")==None:
        return HttpResponse("未登录")

    return HttpResponse("awdaw")


def createOrder(request):
    json_data = json.load(request.body)
    user_id = request.session.get("user_id")


    order.objects.create(order_id=time.strftime("%Y%m%d%H%M%S"), sellerAddress=json_data.get("sellerAddress"), sellerPhone=json_data.get("sellerPhone"),
    sellerName=json_data.get("sellerName"), seller_id=json_data.get("seller_id"), buyersAddress=json_data.get("buyersAddress"), buyersPhone=json_data.get("buyersPhone"),
    buyersName=json_data.get("buyersName"), buyers_id=json_data.get("buyers_id"))

    redata = {
        'code': 200,
        'msg': '创建成功',
        'data': None
    }
    return HttpResponse(json.dumps(redata, indent=4))


def storeList(request):
    # json_data = json.load(request.body)
    # user_id = request.session.get("user_id")
    #查詢

    shopList= shops.objects.all()
    i=0
    data={}
    for shop in shopList:
        data[i]={
            'shop_id':shop.shop_id,
            'price':shop.price,
            'imgUrl':shop.imgUrl,
            'title':shop.title,
            'seller_id':shop.seller_id,
            'sellerImg':"",
        }
        i=i+1



    redata = {
        'code': 200,
        'msg': '获取成功',
        'data': data,
    }
    return HttpResponse(json.dumps(redata, indent=4))

def shopDetailed(request):
    id= request.POST.get("id")
    shopList= shops.objects.get(shop_id=id)
    print(shopList)
    data={
            'shop_id':shopList.shop_id,
            'price':shopList.price,
            'imgUrl':shopList.imgUrl,
            'title':shopList.title,
            'seller_name':'超级废品家',
            'sellerImg':"",
            'crdate':shopList.crdate.strftime("%Y-%m-%d"),
            'content':shopList.content,
        }

    redata = {
        'code': 200,
        'msg': '获取成功',
        'data': data,
    }
    return HttpResponse(json.dumps(redata, indent=4))



def add_img(request):



    if request.method == 'POST':
        files = request.FILES.getlist('file')  # 获取
        # 储存
        import os
        import time
        urllist={}
        i=0
        print(files)
        for fs in files:
            # 时间戳
            t = time.time()
            t = int(round(t * 1000))  # 毫秒
            file_name = str(t) + os.path.splitext(fs.name)[1]
            print(file_name)
            filename = os.path.join(settings.MEDIA_ROOT, 'img', file_name)
            urllist[i] = '/media/img/' + filename
            i=i+1
            print(i)
            with open(filename, 'wb') as f:
                data = fs.file.read()
                f.write(data)

        redata = {
                'code': 200,
                'msg':'上传成功',
                'url':urllist
            }
        return HttpResponse(json.dumps(redata, indent=4))
