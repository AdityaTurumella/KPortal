from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/authentication/login/")
def homepage(request):
    return render(request,"expenses/index.html")
