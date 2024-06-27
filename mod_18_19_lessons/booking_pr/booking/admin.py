from django.contrib import admin
from .models import Booking, ExtraService, Tour, Tourist


admin.site.register(Booking)
admin.site.register(Tour)
admin.site.register(ExtraService)
admin.site.register(Tourist)
