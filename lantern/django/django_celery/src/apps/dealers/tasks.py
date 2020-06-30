from datetime import timedelta

from django.utils import timezone
from rest_framework.authtoken.models import Token

from common.celery import app


@app.task()
def refresh_dealer_tokens():
    now = timezone.now()
    tokens = Token.objects.filter(created__lte=now - timedelta(days=7))

    for token in tokens:
        token.key = token.generate_key()
        token.created = now
        # token.save()  #  10k db requests

    Token.objects.bulk_update(tokens, fields=['key', 'created'])
    print('Tokens have been refreshed')

