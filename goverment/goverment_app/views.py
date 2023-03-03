from django.contrib import messages
from django.shortcuts import render, redirect
from goverment_app.models import registertable, policytable, aadharcardtable


def aboutpage(request):
    return render(request, 'about.html')


def signUpPage(request):
    return render(request, 'signup.html')


def addData(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        middlename = request.POST.get('middle_name')
        lastname = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cast = request.POST.get('cast')
        disabilityStatus = request.POST.get('disabilityStatus')
        minorityStatus = request.POST.get('minorityStatus')
        BPLStatus = request.POST.get('BPLStatus')
        ResidenceArea = request.POST.get('ResidenceArea')

        query = aadharcardtable(firstname=firstname, middlename=middlename, lastname=lastname, phonenumber=phone_no,
                                dob=age, gender=gender, cast=cast, DisabilityStatus=disabilityStatus,
                                MinorityStatus=minorityStatus, BPLStatus=BPLStatus, ResidenceArea=ResidenceArea)
        query.save()

    else:
        pass

    return render(request, 'index.html')


def fetchdata(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        occupation = request.POST.get("occupation")
        password = request.POST.get("con_password")
        mobile_no = request.POST.get("phone_no")

        query = registertable(Full_Name=name, Email=email, Occupation=occupation, Password=password,
                              Mobile_no=mobile_no)
        query.save()
        messages.success(request, 'YOU ARE REGISTERED NOW ')

    else:
        messages.error(request, "error")

    return render(request, "index.html")


def loginpage(request):
    return render(request, 'login.html')


def addDetailpage(request):
    return render(request, 'addDetail.html')


def checklogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        try:
            check = registertable.objects.get(Email=email, Password=password)
            request.session['loginid'] = check.id
            request.session['loginname'] = check.Full_Name

        except:
            check = None

        if check and check.id is not None:
            return render(request, "index.html")
        else:
            return render(request, "login.html")

    else:
        pass

    return render(request, 'login.html')


def contactpage(request):
    return render(request, 'contact.html')


def indexpage(request):
    return render(request, 'index.html')


def detailpage(request, id):
    query = policytable.objects.get(id=id)
    details = {
        'data': query
    }
    return render(request, 'detail.html', details)


def schemespage(request):
    query = policytable.objects.all()
    details = {
        'data': query
    }
    return render(request, 'schemes.html', details)


def featurepage(request):
    return render(request, 'feature.html')


def teampage(request):
    return render(request, 'team.html')


def testimonialpage(request):
    return render(request, 'testimonial.html')


def logout(request):
    try:
        del request.session['loginid']
        del request.session['loginname']

    except:
        print("jdsgjbf")
        pass
    return redirect(indexpage)
