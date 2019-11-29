from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    allProds = []
    catprods = Product.objects.values('category', 'id')
    # print(catprods)
    # print("\nss\n")
    cats = {item['category'] for item in catprods}
    print(cats)
    # i = 0
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        # print(prod, "ssldie", nSlides)
        allProds.append([prod, range(1, nSlides), nSlides])
        # print(" the value of i ", str(i))
        # print(allProds)
        # i += 1
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        # print("request")
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodView(request, myid):
    product = Product.objects.filter(id=myid)
    # print(product.product_name)
    return render(request, 'shop/prodView.html', {'product': product[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')
