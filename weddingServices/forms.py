from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone
from datetime import datetime, date

from .models import HallBooking, CatererBooking, FloristBooking
from multiselectfield import MultiSelectFormField

TIME_SLOTS = (
	('forenoon', 'Forenoon [8-12]'),
	('afternoon', 'Afternoon [2-5]'),
	('evening', 'Evening [6-10]')
	)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class BookingHallForm(forms.ModelForm):
	booking_date = forms.DateField(
		widget=SelectDateWidget(), required=True,
		help_text='Required. Enter a valid date.', initial=timezone.now())
	time_slots = MultiSelectFormField(
		choices=TIME_SLOTS,
		help_text='Required. Enter valid time slots.')

	class Meta:
		model = HallBooking
		fields = ('booking_date', 'time_slots')

	def __init__(self, *args, **kwargs):
		self.pk = kwargs.pop('pk', None)
		super(BookingHallForm, self).__init__(*args, **kwargs)

	#called on validation of the form
	def clean_booking_date(self):
		booking_date = self.cleaned_data.get('booking_date')
		if HallBooking.objects.all().filter(booking_date=booking_date).filter(hall_id=int(self.pk)):
			self.add_error('booking_date', "Sorry Date is already booked. Please choose another.")
		return booking_date

class BookingCatererForm(forms.ModelForm):
	booking_date = forms.DateField(
		widget=SelectDateWidget(), required=True,
		help_text='Required. Enter a valid date.', initial=timezone.now())
	time_slots = MultiSelectFormField(
		choices=TIME_SLOTS, help_text='Required. Enter valid time slots.')
	
	class Meta:
		model = CatererBooking
		fields = ('booking_date', 'time_slots')

	def __init__(self, *args, **kwargs):
		self.pk = kwargs.pop('pk', None)
		super(BookingCatererForm, self).__init__(*args, **kwargs)

	#called on validation of the form
	def clean_booking_date(self):
		booking_date = self.cleaned_data.get('booking_date')
		if CatererBooking.objects.all().filter(booking_date=booking_date).filter(caterer_id=int(self.pk)):
			self.add_error('booking_date', "Sorry Date is already booked. Please choose another.")
		return booking_date

class BookingFloristForm(forms.ModelForm):
	booking_date = forms.DateField(
		widget=SelectDateWidget(), required=True,
		help_text='Required. Enter a valid date.', initial=timezone.now())
	time_slots = MultiSelectFormField(
		choices=TIME_SLOTS,
		help_text='Required. Enter valid time slots.')

	class Meta:
		model = FloristBooking
		fields = ('booking_date', 'time_slots')

	def __init__(self, *args, **kwargs):
		self.pk = kwargs.pop('pk', None)
		super(BookingFloristForm, self).__init__(*args, **kwargs)

	#called on validation of the form
	def clean_booking_date(self):
		booking_date = self.cleaned_data.get('booking_date')
		if FloristBooking.objects.all().filter(booking_date=booking_date).filter(florist_id=int(self.pk)):
			self.add_error('booking_date', "Sorry Date is already booked. Please choose another.")
		return booking_date
