from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'store/index.html', )


def blog(request):

    context = {'title': 'Blog'}

    # return HttpResponse('blog Page', context)
    return render(request, 'store/blog.html', context)


def about(request):

    context = {'title': 'About'}

    # return HttpResponse('About Page')
    return render(request, 'store/about.html', context)


def orders(request):

    context = {'title': 'My Orders'}

    # return HttpResponse('blog Page', context)
    return render(request, 'store/orders.html', context)


def profile(request):

    context = {'title': 'Profile'}
    # return HttpResponse('User Profile', context)
    return render(request, 'store/profile.html', context)


def cart(request):
    context = {'title': 'Cart'}
    # return HttpResponse('Cart Page')
    return render(request, 'store/cart.html', context)


def contact(request):

    context = {'title': 'Contact'}

    return render(request, 'store/contact.html', context)
    # return HttpResponse('Contact Page')