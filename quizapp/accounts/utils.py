from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from decouple import config


def send_registration_email(user_email, user):
    subject = 'Welcome to Our Website'
    html_message = render_to_string('email/email_template.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = config('EMAIL_SENDER')
    recipient_list = [user_email]

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
