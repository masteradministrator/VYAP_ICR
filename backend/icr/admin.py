from django.contrib import admin

# Register your models here.
from .models import InwardCourierRegistry





class ICRA(admin.ModelAdmin):
	list_display = ['airway_bill_number','senders_name','recivers_name','timestamp','courier_service_used','origin_of_the_courier','destination_of_the_courier']
	search_fields = ['airway_bill_number', 'recivers_name', 'senders_name','timestamp','courier_service_used','origin_of_the_courier','destination_of_the_courier' ]
	
	# class Meta:
	# 	model = InwardCourierRegistry



admin.site.register(InwardCourierRegistry,ICRA)
