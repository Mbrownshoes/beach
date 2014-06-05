from django.test import TestCase
from django.core.exceptions import ValidationError
import datetime
from django.utils import timezone

from balmy_beach.models import WaterT, AirT, WaterQuality

class AllModelTest(TestCase):

    def test_saving_and_retrieving_items(self):

        first_item = WaterT()
        first_item.surf_temp = '90'
        first_item.meas_date = timezone.now() + datetime.timedelta(days=-5)
        print(first_item.surf_temp)
        first_item.save()

        first_item = AirT()
        first_item.air_temp = '10'
        print(first_item.air_temp)
        first_item.save()

        first_item = WaterQuality()
        first_item.ecoli = '20'
        print(first_item.ecoli)
        first_item.save()