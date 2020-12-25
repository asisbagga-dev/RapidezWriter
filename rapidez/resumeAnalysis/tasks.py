from celery import shared_task
from time import sleep
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email():
    try:
        print("Sending email")
        email_from = settings.EMAIL_ADMIN
        email_to = 'bharath.nr1@gmail.com'

        content = 'Test email'

        #message1 = ('Quote request', 'Have attached the pdf with the required materials', email_from, [email_to])
        #message2 = ('New comedian registration', content , email_from, [email_admin])
        #send_mass_mail((message1, message2), fail_silently=False)
        send_mail(
            'Resume received',
            'Have attached the resume requested for review.',
            email_from,
            [email_to],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print("Unable to send email : " + str(e))
    