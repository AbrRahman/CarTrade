from django.shortcuts import render,redirect
from cars.models import CarModel
from profiles.models import OrderModel
from cars.forms import CommentForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
class CarDetailsView(DetailView):
    model=CarModel
    template_name="car_details.html"
    pk_url_kwarg='id'

    def post(self,request,*args,**kwargs):
        form=CommentForm(data=self.request.POST)
        car=self.get_object()
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.car=car
            form.save()
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        car=self.object
        print(car.description)
        comments=car.comment.all()
        form=CommentForm()
        context['comments']=comments
        context['form']=form
        context['car']=car
        return context
    
@login_required
def buy_product(request,id):
    product=CarModel.objects.get(pk=id)
    if product.quantity>0:
        product.quantity-=1
    product.save()
    order = OrderModel.objects.filter(car=product, user=request.user).first()
    if order is None:
        order = OrderModel.objects.create(car=product, user=request.user, quantity=1)
    else:
        order.quantity += 1
    order.save()
    return redirect(reverse('car_details', args=[id]))


