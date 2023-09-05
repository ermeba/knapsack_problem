from django.db import models
from client.models import UserProfileInfo
from django.utils import timezone
from django.urls import reverse


# Create your models here.
appliances_choices = (('', 'None'),
                      ('Coffee maker', 'Coffee maker - 1200 Watts'),
                      ('Clothes washer', 'Clothes washer - 500 Watts'),
                      ('Clothes dryer', 'Clothes dryer - 5000 Watts'),
                      ('Dishwasher', 'Dishwasher - 2400 Watts'),
                      ('Hair dryer', 'Hair dryer - 1875 Watts'),
                      ('Heater', 'Heater - 1500 Watts'),
                      ('Clothes iron', 'Clothes iron - 1800 Watts'),
                      ('Microwave oven', 'Microwave oven - 1100 Watts'),
                      ('Laptop', 'Laptop - 50 Watts'),
                      ('Radio', 'Radio - 400 Watts'),
                      ('Refrigerator', 'Refrigerator - 725 Watts'),
                      ('Television', 'Television - 110 Watts'),
                      ('Vacuum cleaner', 'Vacuum cleaner - 1440 Watts'),
                      ('Water pump', 'Water pump - 1100 Watts'),
                      ('Toaster', 'Toaster - 1400 Watts'),
                      ('Ceiling Fans', 'Ceiling Fans - 110 Watts'),)

priority_choices = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
                    (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'),
                    (18, '18'), (19, '19'), (20, '20'))


class KnapsackResults(models.Model):
    profile = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='knapsack')
    appliance1 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance2 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance3 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance4 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance5 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance6 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance7 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance8 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance9 = models.CharField(choices=appliances_choices, default='', max_length=30)
    appliance10 = models.CharField(choices=appliances_choices, default='', max_length=30)
    priority1 = models.IntegerField(choices=priority_choices, default=0)
    priority2 = models.IntegerField(choices=priority_choices, default=0)
    priority3 = models.IntegerField(choices=priority_choices, default=0)
    priority4 = models.IntegerField(choices=priority_choices, default=0)
    priority5 = models.IntegerField(choices=priority_choices, default=0)
    priority6 = models.IntegerField(choices=priority_choices, default=0)
    priority7 = models.IntegerField(choices=priority_choices, default=0)
    priority8 = models.IntegerField(choices=priority_choices, default=0)
    priority9 = models.IntegerField(choices=priority_choices, default=0)
    priority10 = models.IntegerField(choices=priority_choices, default=0)
    time1 = models.IntegerField(default=0)
    time2 = models.IntegerField(default=0)
    time3 = models.IntegerField(default=0)
    time4 = models.IntegerField(default=0)
    time5 = models.IntegerField(default=0)
    time6 = models.IntegerField(default=0)
    time7 = models.IntegerField(default=0)
    time8 = models.IntegerField(default=0)
    time9 = models.IntegerField(default=0)
    time10 = models.IntegerField(default=0)
    predicted_on = models.DateTimeField(default=timezone.now)
    price_of_electricity = models.IntegerField(default=0)
    price_of_high_tariffs = models.IntegerField(default=0)
    limit_of_time_hours = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('knapsack:knapsack', kwargs={'pk': self.profile.pk})
