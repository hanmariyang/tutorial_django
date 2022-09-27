import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{'name':'족발', 'price':30000}, {'name':'햄버거', 'price':9000}, {'name':'치킨', 'price':20000}, {'name':'초밥', 'price':15000}, {'name':'피자', 'price':24000}, {'name':'짜장면', 'price':60000}, {'name':'떡볶이', 'price':5000}]
    pick = random.choice(menus)
    contxt = {
        'pick' : pick,
        'name' : name,
        'menus' : menus,
    }
    return render(request, 'dinner.html', contxt)