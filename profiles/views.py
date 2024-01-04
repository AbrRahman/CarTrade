from django.shortcuts import render,redirect
from profiles.forms import RegisterForm,ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from profiles.models import OrderModel
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

@login_required
def user_profile(request):
    order = OrderModel.objects.filter(user=request.user)
    return render(request,'profile.html',{"orders":order})


# method_decorator(login_required,name='dispatch')
class RegisterClassView(CreateView):
    model = User
    template_name='register.html'
    form_class = RegisterForm
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        form.instance.author=self.request.user
        messages.success(self.request,"Register Successfully")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.success(self.request,"Register Failed")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']="Register"
        return context


# log in view
class UserLoginView(LoginView):
    template_name="login.html"
    def get_success_url(self):
        return reverse_lazy("profiles")
    
    def form_valid(self,form):
        messages.success(self.request,"Logged In Success")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,"Logged In Failed")
        return super().form_invalid(form)

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,"Logged In  Successfully")
    return redirect("home")

@login_required
def profile_edit(request):
    if request.method=="POST":
        form=ChangeUserForm(request.POST,instance=request.user)        
        if form.is_valid():
                form.save()
                messages.success(request,"Profile edit  Successfully")
                return redirect('profiles')
    else:
         form=ChangeUserForm(instance=request.user)
    return render(request,"register.html",{'form':form,'type':"Edit"})
