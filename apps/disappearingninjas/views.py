from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {}
    context['image'] = 'none'
    return render(request, 'disappearingninjas/index.html', context)

def all(request):
    context = {}
    context ['image'] = 'ninjas'
    return render(request, 'disappearingninjas/ninjas.html', context)

def show(request, color):
    context = {}
    if color == 'red':
        context ['image']= 'raphael'
    elif color == 'blue':
        context ['image'] = 'leonardo'
    elif color == 'purple':
        context ['image'] = 'donatello'
    elif color == 'orange':
        context ['image'] = 'michelangelo'
    else:
        context ['image'] = 'april'
    return render(request,'disappearingninjas/index.html', context)
