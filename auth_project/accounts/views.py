from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# 🔐 LOGIN VIEW
def login_view(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/landing/')   # 🚀 GO TO SPLASH PAGE

    return render(request, 'login.html')


# 🚪 LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('/login/')
