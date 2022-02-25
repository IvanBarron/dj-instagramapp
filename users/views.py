import profile
from django.shortcuts import render, redirect
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.utils import IntegrityError

from django.contrib.auth.models import User
from .models import Profile


class LoginProfile(views.LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('posts:feed')


class LogoutProfile(LoginRequiredMixin, views.LogoutView):
    next_page = reverse_lazy('users:login')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, "users/signup.html", {
                'error':'Password confirmation does not match'
            })

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        try:

            user = User.objects.create_user(username=username, password=password, email=email,
                                            first_name=first_name, last_name=last_name)

            profile = Profile(user=user)
            profile.save()
        except IntegrityError:
            return render(request, "users/signup.html", {
                'error':'Username or email already used.'
            })

        return redirect('users:login')

    return render(request,"users/signup.html")


def update_profile(request):
    return render(request, "users/update_profile.html")