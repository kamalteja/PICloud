from django.contrib import admin

from services.models import services
# Register your models here.

class servicesModelAdmin (admin.ModelAdmin):
	list_display = ["__unicode__", "last_updated_time"]
	class Meta:
		model = services

admin.site.register(services, servicesModelAdmin)

