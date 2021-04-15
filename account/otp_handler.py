from random import randint
from .models import User
from datetime import datetime


def create_otp():
    return randint(1000, 9999)


def send_otp(phone, otp):
    print("OTP = {}".format(otp))


def check_otp_expiration(phone):
    try:
        user = User.objects.get(phone=phone)
        now = datetime.now()
        otp_time = user.otp_create_time
        passed_time = now - otp_time
        print(passed_time)
        return False
    except User.DoesNotExist:
        return False
