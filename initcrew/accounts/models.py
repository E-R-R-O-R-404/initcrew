from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ExtendedUser(models.Model):
    phone_num = models.CharField(max_length=15, blank=True)
    is_purchased = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __bool__(self):
        return self.is_purchased

   