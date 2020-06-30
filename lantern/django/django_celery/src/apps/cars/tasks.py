from django.core.mail import send_mail
from rest_framework.authtoken.models import Token

from apps.newsletters.models import Newsletter
from common.celery import app


@app.task()
def send_notification(car_id: int):
    from apps.cars.models import Car

    car = Car.objects.filter(id=car_id, status=Car.STATUS_PUBLISHED)

    emails = Newsletter.objects.all().values_list('email', flat=True)

    print('Working...')

    # send_mail(subject=f'New car: {car}',
    #           message='Hello boy/girl..',
    #           recipient_list=emails,
    #           from_email='settings.from_mail@gmail.com')
    #
    # other logic: log in history notifications
    #
    Token