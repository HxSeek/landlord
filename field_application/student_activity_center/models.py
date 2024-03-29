#-*- coding: utf-8 -*-
import copy
from datetime import datetime, timedelta, date

from django.db import models

from field_application.account.models import Organization 
from field_application.models.models import RoomApplication
from field_application.models.mixin import DateMixin


class StudentActivityCenterApplication(RoomApplication, DateMixin):

    activity = models.CharField(max_length=30)
    activity_summary = models.CharField(max_length=200)
    sponsor = models.CharField(max_length=30, blank=True, null=True)
    sponsorship = models.CharField(max_length=30, blank=True, null=True)
    sponsorship_usage = models.CharField(max_length=40, blank=True, null=True)
    
    def submit(self):

        self.clean_date()

        return self.save()


