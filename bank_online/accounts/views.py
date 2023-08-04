from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.models import Person
from bankingapp.models import District, Branch


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'signup.html')

        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def signin(request):
    district_list = District.objects.all()
    branch = Branch.objects.all()
    return render(request, 'form.html', {'district_list': district_list, 'branch': branch})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def new(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district_id = request.POST['district']
        branch_id = request.POST['branch']

        if Person.objects.filter(email=email).exists():
            messages.error(request, "Email is Taken")
            return redirect('signin')

        else:

            try:
                selected_district = District.objects.get(id=district_id)
            except District.DoesNotExist:
                return HttpResponse('Please check the District')

            try:
                selected_branch = Branch.objects.get(id=branch_id, district=selected_district)
            except Branch.DoesNotExist:
                return HttpResponse('Please check the Branch')

            person = Person.objects.create(name=name, dob=dob, age=age, address=address,
                                           phone=phone, email=email,
                                           district=selected_district,
                                           branch=selected_branch)
            person.save()

            messages.info(request, "Application is Successful")
            return redirect('/')

    return render(request, 'index.html')

