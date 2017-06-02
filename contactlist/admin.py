from django.contrib import admin
from .models import Contact

# Register Contact models here.
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'contact_number']
admin.site.register(Contact, ContactAdmin)