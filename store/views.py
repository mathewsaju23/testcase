from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from apiapp.models import UserCart
# Create your views here.


def store(request):
    context = {'user': request.user}
    print(request.user)
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def signup(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        cart = UserCart.objects.create(user=myuser)
        cart.save()

        messages.success(request, "Account created Successfully")
        return redirect('signin')

    return render(request, 'store/signup.html', context)


def signin(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            print("user", user)
            return render(request, "store/store.html", {'fname': fname, 'user': user})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('store')

    return render(request, 'store/signin.html', context)


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('store')
