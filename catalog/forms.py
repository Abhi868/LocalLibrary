
import datetime
from django import forms
from django.core.exceptions import ValidationError
#from django.utils.translation import ugettext_lazy as_

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
	email_id=forms.EmailField(help_text="Enter your valid EmailId")
				# bio=forms.TextField(max_length=500,help_text="Tell Us something about yourself")

	class Meta:
		model=User
		fields=['username','password1','password2','email_id']


class BookRenewForm(forms.Form):
	renewal_date=forms.DateField(help_text="Enter Renewal date between today's date to 3 weeks in future")


	def clean_renewal_date(self):
		data=self.cleaned_data('renewal_date')

		if data<datetime.date.today():
			raise Vqalidation_Error("Invalid date as date has been passed")

		if data>datetime.date.today() + datetime.timedelta(weeks=4):
			raise validationError("dEntered date if aftter 4 weeks from the today's date")

		return data