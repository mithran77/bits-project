from django.db import models
from django.utils import timezone
from decimal import Decimal
from multiselectfield import MultiSelectField

# Constants
#FORENOON = 'FN'
#AFTERNOON = 'AN'
#EVENING = 'EV'

class Hall(models.Model):
    user = models.ForeignKey('auth.User')
    shop_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=70,blank=True)
    session_cost = models.DecimalField(
		max_digits=6, decimal_places=2, default=Decimal('0.0000'))
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.shop_name

class Caterer(models.Model):
    user = models.ForeignKey('auth.User')
    shop_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=70,blank=True)
    session_cost = models.DecimalField(
		max_digits=6, decimal_places=2, default=Decimal('0.0000'))
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.shop_name

class Florist(models.Model):
    user = models.ForeignKey('auth.User')
    shop_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=70,blank=True)
    session_cost = models.DecimalField(
		max_digits=6, decimal_places=2, default=Decimal('0.0000'))
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.shop_name

class HallBooking(models.Model):
    TIME_SLOTS = (
	('FN', 'Forenoon [8-12]'),
	('AN', 'Afternoon [2-5]'),
	('EV', 'Evening [6-10]')
	)
    user = models.ForeignKey('auth.User', related_name='hall_user')
    hall = models.ForeignKey(Hall, related_name='hall')
    booking_date = models.DateField(default=timezone.now, max_length=50)
    time_slots = MultiSelectField()
    cost = models.DecimalField(
		max_digits=6, decimal_places=2, default=Decimal('0.0000'))
	
class CatererBooking(models.Model):
    TIME_SLOTS = (
	('FN', 'Forenoon [8-12]'),
	('AN', 'Afternoon [2-5]'),
	('EV', 'Evening [6-10]')
	)
    user = models.ForeignKey('auth.User', related_name='caterer_user')
    caterer = models.ForeignKey(Caterer, related_name='hall')
    booking_date = models.DateField(default=timezone.now, max_length=50)
    time_slots = MultiSelectField()
    cost = models.DecimalField(
		max_digits=6, decimal_places=2, default=Decimal('0.0000'))

class FloristBooking(models.Model):
    TIME_SLOTS = (
	('FN', 'Forenoon [8-12]'),
	('AN', 'Afternoon [2-5]'),
	('EV', 'Evening [6-10]')
	)
    user = models.ForeignKey('auth.User', related_name='florist_user')
    florist = models.ForeignKey(Florist, related_name='hall')
    booking_date = models.DateField(default=timezone.now, max_length=50)
    time_slots = MultiSelectField()
    cost = models.DecimalField(
		max_digits=6, decimal_places=2, default=Decimal('0.0000'))
