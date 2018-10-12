
import datetime
from django import forms
from django.core.exceptions import ValidationError
#from django.utils.translation import ugettext_lazy as_

class BookRenewForm(forms.Form):
	renewal_date=forms.DateField(help_text="Enter Renewal date between today's date to 3 weeks in future")


	def clean_renewal_date(self):
		data=self.cleaned_data('renewal_date')

		if data<datetime.date.today():
			raise Vqalidation_Error("Invalid date as date has been passed")

		if data>datetime.date.today() + datetime.timedelta(weeks=4):
			raise validationError("dEntered date if aftter 4 weeks from the today's date")

		return data