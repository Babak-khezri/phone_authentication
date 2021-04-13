from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from . models import User
# Create your views here.


def register_view(request):
    form = UserForm
    if request.method == 'POST':
        if 'phone' in request.POST:
            phone = request.POST.get('phone')
            try:
                user = User.objects.get(phone=phone)
            except:
                pass
            print(phone)
    return render(request, 'registration/register.html', {'form': form})


def dashboard_view(request):
    return render(request, 'registration/dashboard.html')
