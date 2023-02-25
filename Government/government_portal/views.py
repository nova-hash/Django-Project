from distutils.command import check

from django.contrib import messages
from django.shortcuts import render
from .models import registertable


def indexpage(request):
    return render(request, 'index.html')


def fetchdata(request):
    if request.method == 'POST':
        name = request.POST.get("Full_Name")
        email = request.POST.get("Email")
        address = request.POST.get("Password")
        Password = request.POST.get("Password")
        Mobile_no = request.POST.get("Mobile_no")

        query = registertable(Full_Name=name, Email=email, Address=address, Password=Password, Mobile_no=Mobile_no)
        query.save()
        messages.success(request, 'YOU ARE REGISTERED NOW ')

    else:
        messages.error(request, "error ")

    return render(request, "login.html")


def loginpage(request):
    return render(request, 'login.html')

def dashboardpage(request):
    if(check.id != None):
        dash = "dashboard.html"
    else:
        dash = "login.html"
    return render(request, dash)

def checklogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        print(username)
        try:
            check = registertable.objects.get(Full_Name=username, Password=password)
            request.session['loginid'] = check.id
            request.session['loginname'] = check.Full_Name


        except:
            check = None




        if check and check.id is not None:
            return render(request, "dashboard.html")
        else:
            return render(request, "login.html")

    else:
        pass

    return render(request, 'login.html')

# Create your views here.

def logout(request):
    try:
        del request.session['loginid']
        del request.session['loginname']
    except:
        pass
    return  render(request,'login.html')

