from django.db import models

# Create your models here.
from common.models import BaseDateAuditModel


class Newsletter(BaseDateAuditModel):
    email = models.EmailField
