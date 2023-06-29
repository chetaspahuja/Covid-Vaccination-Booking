from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import userBooking, VaccinationCenters, AdminData


@login_required(login_url='login')
# Create your views here.
def HomePage(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if(pass1 != pass2):
            return HttpResponse("Your Passwords don't match")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user = authenticate(request, username=uname, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is Incorrect")
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def bookingPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email_id = request.POST.get('email_id')
        mobile_number = request.POST.get('mnumber')
        sex = request.POST.get('sex')
        slot_date = request.POST.get('slot_date')
        center_name = request.POST.get('center_name')

        center = VaccinationCenters.objects.get(centre_name=center_name)

        if center.empty_slots == 0:
            return HttpResponse("Sorry, slots not available, try again")
        else:
            center.empty_slots = center.empty_slots-1
            center.save()

            input = userBooking(name=name, age=age, email_id=email_id,
                                mobileNum=mobile_number, sex=sex, date=slot_date, center_name=center_name)
        # import pdb;pdb.set_trace()
            input.save()
    # import pdb;pdb.set_trace()
    return render(request, 'home.html')


def test(request):
    centers = VaccinationCenters.objects.all()
    return render(request, 'selectDate.html', {'centers': centers})


def selectDate(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        centers = VaccinationCenters.objects.filter(date=date)
        return render(request, 'booking.html', {'centers': centers})

    return render(request, 'selectDate.html')

# ---------------------- admin functions --------------------------------


def LoginPageAdmin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')

        try:
            admin = AdminData.objects.get(user_name=uname, password=pass1)
            return redirect('homeAdmin')
            # return render(request,'homeAdmin')
        except AdminData.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'loginAdmin.html')


def AdminHomePage(request):
    centers = VaccinationCenters.objects.all()
    return render(request, 'homeAdmin.html', {'centers': centers})


def home(request):
    centers = centers.objects.all()
    return render(request, 'home.html', {'centers': centers})


def update_slots(request, centre_name):
    center = get_object_or_404(VaccinationCenters, centre_name=centre_name)
    name = center.name
    center_address = center.center_address
    
    if request.method == "POST":
        date = request.POST.get("date")
        empty_slots = request.POST.get("empty_slots")

        try:
            record = VaccinationCenters.objects.get(centre_name=centre_name, date=date)
            record.empty_slots = empty_slots
            record.save()
        except VaccinationCenters.DoesNotExist:
            name = center.name
            center_address = center.center_address
            new_record = VaccinationCenters(name=name, centre_name=centre_name, center_address=center_address, date=date, empty_slots=empty_slots)
            new_record.save()

        messages.success(request, 'Slots updated successfully.')
        return redirect('homeAdmin')

    return render(request, 'update_slots.html', {'center': center})


def delete_center(request, centre_name):
    center = get_object_or_404(VaccinationCenters, centre_name=centre_name)
    center.delete()
    messages.success(request, 'Center deleted successfully.')
    return redirect('homeAdmin')


def add_center(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        center_name = request.POST.get('centre_name')
        center_address = request.POST.get('center_address')
        empty_slots = request.POST.get('empty_slots')
        center = VaccinationCenters(
            name=name, centre_name=center_name, center_address=center_address, empty_slots=empty_slots)
        center.save()
        messages.success(request, 'Center added successfully.')
        return redirect('homeAdmin')

    return render(request, 'add_center.html')
