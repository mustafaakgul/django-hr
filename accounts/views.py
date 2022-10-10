from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, AccountForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404
import logging
from django.contrib.auth.decorators import login_required
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth import (
                                  authenticate,
                                  logout ,
                                  login
                              )
from django.shortcuts import (
                                  render,
                                  get_object_or_404,
                                  redirect
                              )
from .forms import (
                    RegistrationForm,
                    AccountAuthenticationForm,
                    AccountUpdateform
                )
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf import settings


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, "Başarıyla Kayıt Oldunuz...")

        return redirect("dashboard")
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "accounts/login.html", context)

        messages.success(request, "Başarıyla Giriş Yaptınız")
        login(request, user)
        return redirect("dashboard")
    return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yaptınız")
    return redirect("index")


def forgot(request):
    return render(request, "accounts/forgot.html")


def reset(request):
    return render(request, "accounts/reset.html")


def profile(request):
    account = get_object_or_404(Account, id=request.user.id)
    form = AccountForm(request.POST or None, instance = account)
    context = {
        "account": form,
    }

    return render(request, "accounts/settings.html", context)


def login_view(request):
    formLogin = AccountAuthenticationForm(request.POST or None)
    context = {
        "formLogin": formLogin
    }
    user = request.user

    if user.is_authenticated:
        return redirect("current_state")

    if request.method == "POST":
        if formLogin.is_valid():
            # email   = request.POST.get('email')
            # password = request.POST.get('password')
            email = formLogin.cleaned_data["email"]
            password = formLogin.cleaned_data["password"]
            user =  authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "Başarıyla giriş yaptınız.")
                return redirect("current_state")
            else:
                messages.error("please Correct Below Errors")

    return render(request, "accounts/login.html", context)

def registration_view(request):
    formRegister = RegistrationForm(request.POST or None)
    context = {
        "formRegister": formRegister,
    }
    user = request.user

    if user.is_authenticated:
        return redirect("current_state")

    if formRegister.is_valid():
        formRegister.save()
        email    = formRegister.cleaned_data.get('email')
        raw_pass = formRegister.cleaned_data.get('password1')
        account = authenticate(email=email, password = raw_pass)
        login(request, account)
        #login(request, account, backend='django.contrib.auth.backends.ModelBackend')

        user_account = get_object_or_404(Account, email=request.user.email)
        user_account.save()

        messages.success(request, "Kaydı başarıyla tamamladınız. {}".format(request.user.username))
        return redirect('current_state')
    else:
        messages.error(request, "Please Correct Below Errors")

    return render(request, "accounts/register.html", context)


@login_required(login_url = "accounts:authentication")
def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("index")


@login_required(login_url = "accounts:authentication")
def changePassword(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        re_new_password = request.POST.get('re_new_password')
        ok = auth.authenticate(username=username, password=password)
        print(request)
        if ok:
            auth.login(request, ok)
            print("The original account password is correct")
            if new_password:
                print("Password is not empty")
                if new_password == re_new_password:
                    print("The two passwords are the same")
                    request.user.set_password(new_password)
                    request.user.save()
                    return redirect(reverse('login'))
                else:
                    error = "The two passwords are inconsistent"

            else:
                error = "password can not be blank"
        else:
            error = "The original account or password is incorrect"

    return render(request, 'accounts/changePassword.html', context={"error": error})