from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.models import Group
from .forms import RegisterForm
from django.contrib.auth import authenticate,login
# Create your views here.

class HomeView(TemplateView):
    template_name = 'principal/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None

        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name
        
        context['group_name'] = group_name

        return context
    
class RegistrationView(View):

    def get(self, request):
        data = {
            'form' : RegisterForm()
        }
        return render(request,'registration/registration.html',data)

    def post(self, request):
        user_creation_form = RegisterForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
        data = {
            'form' : user_creation_form
        }
        return render(request,'registration/registration.html',data)
    
    

