from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'main/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        massage = request.POST.get('message')

        return HttpResponse(f'Thank you {name}! Massege get')
    return render(request, 'main/contact.html')
