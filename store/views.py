from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render


# Create your views here.


def storehome(request):
    # store/storehome.html

    return render(request, 'store/storehome.html', {'title': 'Welcome To DilSha'})


def aboutus(request):
    return render(request, 'store/aboutus.html', {'title': 'About Us'})


def reviews(request):
    return render(request, 'store/reviews.html', {'title': 'Reviews'})


# def category(request):
#     # store/category.html
#     products = Product.objects.all()
#     return render(request, 'store/category.html', {'title': 'Categories'})


def category(request, category=None):
    if category:
        category = Category.objects.get(name=category)
        products = Product.objects.filter(category=category)
        return render(request, 'store/category.html', {'products': products, 'category': category, 'title': category})
    else:
        products = Product.objects.all()
        return render(request, 'store/category.html', {'products': products, 'title': 'Categories'})


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    # title will be phone name
    return render(request, 'store/product.html', {'product': product, 'title': product.name})


def shop(request, category=None):
    if category:
        category = Category.objects.get(name=category)
        products = Product.objects.filter(category=category)
        return render(request, 'store/shop.html', {'products': products, 'category': category, 'title': category})
    else:
        products = Product.objects.all()
        return render(request, 'store/shop.html', {'products': products, 'title': 'All Phones'})
