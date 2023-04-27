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
    print("------->>>>",total)
    return JsonResponse(total, safe=False)