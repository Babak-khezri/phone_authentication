from account import otp_handler
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import login
from django.urls import reverse
from . models import User
from . import otp_handler
# Create your views here.


def register_view(request):
    form = RegisterForm
    if request.method == 'POST':
        try:
            if 'phone' in request.POST:
                phone = request.POST['phone']
                user = User.objects.get(phone=phone)
                otp = otp_handler.create_otp()
                user.otp = otp
                user.save()
                request.session['user_phone'] = user.phone
                return HttpResponseRedirect(reverse('account:verify'))

        except User.DoesNotExist:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                otp = otp_handler.create_otp()
                user.otp = otp
                user.save()
                request.session['user_phone'] = user.phone
                return HttpResponseRedirect(reverse('account:verify'))

    return render(request, 'registration/register.html', {'form': form})


def verify_view(request):
    phone = request.session.get('user_phone')
    user = get_object_or_404(User, phone=phone)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp_handler.check_otp_expiration(user.phone):
            if user.otp == int(otp):
                user.is_active = True
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse('account:dashboard'))
    return render(request, 'registration/verify.html', {'user': user})


def dashboard_view(request):
    return render(request, 'registration/dashboard.html')
