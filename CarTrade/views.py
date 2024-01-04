from django.shortcuts import render,redirect
from cars.models import CarModel,BrandModel

def landing_page(request):
    return redirect("home")

def home(request,brand_slug=None):
    data=CarModel.objects.all()
    car_brands=BrandModel.objects.all()
    if brand_slug is not None and brand_slug != 'all':
        brand=BrandModel.objects.get(slug=brand_slug)
        data=CarModel.objects.filter(brand=brand)
    for d in data:
        print(d.image)
    return render(request,'home.html',{'cars':data,'brands':car_brands})
