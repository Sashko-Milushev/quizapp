from django.core.mail import send_mail
from decouple import config

def send_registration_email(user_email):
    subject = 'Welcome to Our Website'
    message = 'Thank you for registering on our website.'
    from_email = config('EMAIL_SENDER')
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
