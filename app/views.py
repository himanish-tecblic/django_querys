from django.shortcuts import render
from app.models import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Sum
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def userData(request):
    request.method = "GET"
    user_name = User.objects.all().values()
    if cache.get('name'):
        payload = cache.get('name')
        print(cache.ttl('name'))
    else:
        a = User.objects.all()
        
        payload = []
        for obj in a:
            payload.append(obj.first_name)
            
        cache.set('name',payload, timeout=10)
        
    return JsonResponse(list(user_name),safe=False)


def isDelivered(requset):
    requset.method ="GET"
    Delivered = Order.objects.filter(isDelivered = True).values()
    return JsonResponse(list(Delivered), safe=False)


def Dispatched(requset):
    requset.method ="GET"
    dispatched = Order.objects.filter(dispatched = True).values()
    return JsonResponse(list(dispatched), safe=False)


def PaymentMethod(requset):
    requset.method ="GET"
    Method = Order.objects.filter(paymentMethod = "online").values()
    return JsonResponse(list(Method), safe=False)

def leftpayment(request):
    request.method = "GET"
    a = Order.objects.filter(isDelivered = True).filter(isPaid = False).values()
    return JsonResponse(list(a), safe=False)

def totalSell(request):
    request.method = "GET"
    total = OrderItem.objects.aggregate(Sum("price"))
    print("------->>",total)
    a = int(OrderItem.objects.get(product__name = "A123").price)
    a_name = OrderItem.objects.get(product__name = "A123").product
    b = int(OrderItem.objects.get(product__name = "A721").price)
    b_name = OrderItem.objects.get(product__name = "A721").product
    c = int(OrderItem.objects.get(product__name = "A521").price)
    c_name = OrderItem.objects.get(product__name = "A521").product
    d = int(OrderItem.objects.get(product__name = "A400").price)
    d_name = OrderItem.objects.get(product__name = "A400").product
    e = int(OrderItem.objects.get(product__name = "A200").price)
    e_name = OrderItem.objects.get(product__name = "A200").product
    f = int(OrderItem.objects.get(product__name = "A321").price)
    f_name = OrderItem.objects.get(product__name = "A321").product

    
    lis = [a,b,c,d,e,f]
    print("----->>>", max(lis))
    
    y = max(lis)
    # print(y)
    
    m = OrderItem.objects.filter(price = y).values()
    print("------>>>>>>",m)

    return JsonResponse(list(m), safe=False)



def cancelCount(request):
    request.method = 'GET'
    prod = Product.objects.filter(cancalCount__gt = 4)
    
    return JsonResponse({"data":list(prod.values())}, safe=False)


def getfruits(request):
    
    if cache.get('fruits'):
        payload = cache.get('fruits')
        print(cache.ttl('fruits'))
    else:
        
        objs = fruits.objects.all()
        
        payload = []
        for obj in objs:
            payload.append(obj.fruits_name)
            
        cache.set('fruits',payload, timeout=10)
        
    return JsonResponse({'data' : payload})
