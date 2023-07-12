from django.shortcuts import render

from django.http import HttpResponse
import math

# Create your views here.


def users(request):
    context = {
        'user_name': 'Osama Elnaggar',
        'age': '37',
        'prof': 'Engineer'
    }
    return render(request,'users/users.html', context)

def calculator(request):
    x= math.cos(75)
    y = math.log(50)
    return HttpResponse(x*y)