from django.shortcuts import render
from app.models import *
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Sum

# Create your views here.

def userData(request):
    request.method = "GET"
    user_name = User.objects.all().values()
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
    
    
    
    
    
    x = 34580/10 * 6#target
    
    print("----->>>target", x)
    
    lis = [a,b,c,d,e,f]
    print("----->>>", max(lis))
    
    y = max(lis)
    # print(y)
    
    m = OrderItem.objects.filter(price = y).values()
    print("------>>>>>>",m)

    # for i in lis :
        
    #     # diff = (i - x)
    #     # if Small_diff is None or diff < Small_diff:
    #     #     Small_diff = diff
    #     #     col = i
    #     # print("-------->>>", col)
    #     pass
            
    l = [{str(a_name) : a}, {str(b_name) : b}, {str(c_name) : c}, {str(d_name) : d}, {str(e_name) : e}, {str(f_name) : f}]
    print("--------->>>>", l)
    return JsonResponse(list(m), safe=False)