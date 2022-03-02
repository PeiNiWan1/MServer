
from asyncio.windows_events import NULL
from distutils.log import error

import json
from msilib.schema import Error
from pyexpat import model
from tkinter import E
from django.http import HttpResponse
from ConsumerServer.models import userP, userS
#登录
def user_login(request):
    json_data=json.loads(request.body)
    phone= json_data.get("phone_number")
    user_pa=json_data.get("password")
    #session
    try:
        sql=userS.objects.get(phone_number=phone)
        if(sql!=''):
            if(sql.password==user_pa):
                request.session['user_id']=sql.id
                redata={
                    'code':200,
                    'msg':'登录成功',
                    'session':request.session.session_key,
                    'data':{
                        'user_name':sql.user_name,
                        'nick':sql.user_nick,
                        'img':userP.objects.get(id=sql.id),
                    }
                }
                return HttpResponse(json.dumps(redata,indent=4))
            else:
                redata={
                    'code':500,
                    'msg':'账号密码错误',
                    'data':None
                    }
                return HttpResponse(json.dumps(redata,indent=4))
        else:
            return HttpResponse()
    except userS.DoesNotExist:

        redata={
                    'code':500,
                    'msg':'账号密码错误',
                    'data':'',
                    }
        return HttpResponse(json.dumps(redata,indent=4))



def validation_session(request):
    if( request.session.get('user_id',None)!=None):
        redata={
            'code':200,
            'msg':'有效session',
            'data':None
            }
        return HttpResponse(json.dumps(redata,indent=4))
    else:
        redata={
            'code':500,
            'msg':'无效效session',
            'data':None
            }
        return HttpResponse(json.dumps(redata,indent=4))
def user_register(requset):
    json_data=json.loads(requset.body)

    try:
        userS.objects.get(phone_number=json_data.get("phone_number"))

        redata={
                    'code':500,
                    'msg':'手机号以被注册',
                    'data':None
                    }
        return HttpResponse(json.dumps(redata,indent=4))
    except userS.DoesNotExist:
        userS.objects.create(user_name=json_data.get("user_name"),
            nick=json_data.get("nick"),
            phone_number=json_data.get("phone_number"),
            password=json_data.get("password"),puissance=1)
        user=userS.objects.get(phone_number=json_data.get("phone_number"))
        userP.objects.create(userP_id=user.id)
        redata={
                    'code':200,
                    'msg':'注册成功200',
                    'data':None
                    }
        return HttpResponse(json.dumps(redata,indent=4))


