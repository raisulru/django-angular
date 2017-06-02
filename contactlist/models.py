from django.db import models
from django.core.validators import RegexValidator #Regular expressions validator for contact number

# models for contactlist
class Contact(models.Model):
	name = models.CharField(max_length=200)
	# we validate the contact number by regexvalidator
	contact_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
								   message="number format must be: '+999999999'. Up to 15 digits allowed.")
	contact_number = models.CharField(validators=[contact_regex], max_length=15)
	# we include this field for showing the admin who created the contactlist
	admin = models.ForeignKey('auth.User', related_name='contactlist', on_delete=models.CASCADE)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name
