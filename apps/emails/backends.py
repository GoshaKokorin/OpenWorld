import random
from django.core.mail import send_mail
from altay_backend.config import EMAIL_HOST_USER


def generate_code():
    code = random.randint(100000, 999999)
    return code


def send_verification_mail(email, code):
    subject = 'Altay verification code'
    message = f'Your verification code:\n{code}\nThanks for using Altay.'
    from_email = EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, from_email, recipient_list)


def send_refresh_password_mail(email, code):
    subject = 'Altay refresh password code'
    message = f'Your refresh password code:\n{code}\nThanks for using Altay.'
    from_email = EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, from_email, recipient_list)
