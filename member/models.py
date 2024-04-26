from django.db import models
from common.models import CommonModel


class Member(CommonModel):
    member_email = models.EmailField(max_length=100, unique=True)
    member_password = models.CharField(max_length=100)
    auth_group = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    mem_waiting = models.BooleanField(default=False)
    mem_number = models.CharField(max_length=20)
