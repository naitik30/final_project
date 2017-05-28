from django.contrib import admin
from .models import user_contact,user_details
# Register your mode
# ls here.
admin.site.register(user_contact)
admin.site.register(user_details)
