from django.db import models

# Create your models here.

class InwardCourierRegistry(models.Model):

	senders_code = models.CharField(max_length=10, blank=True, null=True)
	senders_company = models.CharField(max_length=100, blank=True, null=True)
	senders_address = models.CharField(max_length=3000, blank=True,null=True)
	senders_city = models.CharField(max_length=3000, blank=True,null=True)
	senders_name = models.CharField(max_length=3000, blank=True,null=True)
	senders_phoneno = models.CharField(max_length=3000, blank=True,null=True)
	senders_pincode = models.CharField(max_length=3000, blank=True,null=True)
	senders_state = models.CharField(max_length=3000, blank=True,null=True)
	senders_email = models.EmailField()
	recivers_code = models.CharField(max_length=10, blank=True,null=True)
	recivers_company = models.CharField(max_length=3000, blank=True,null=True)
	recivers_address = models.CharField(max_length=3000, blank=True,null=True)
	recivers_name = models.CharField(max_length=3000, blank=True,null=True)
	recivers_phoneno = models.CharField(max_length=3000, blank=True,null=True)
	recivers_pincode = models.CharField(max_length=3000, blank=True,null=True)
	recivers_state = models.CharField(max_length=3000, blank=True,null=True)
	recivers_email = models.EmailField()
	special_instructions = models.CharField(max_length=8000, blank=True,null=True)
	service_sticker = models.CharField(max_length=3000, blank=True,null=True)
	original_senders_name = models.CharField(max_length=3000, blank=True,null=True)
	timestamp = models.DateTimeField()
	courier_service_used = models.CharField(max_length=3000, blank=False,null=False)
	courier_pickedup_by_name = models.CharField(max_length=3000, blank=True,null=True)
	pickup_empid = models.CharField(max_length=3000, blank=True,null=True)
	timestamp = models.DateTimeField( auto_now_add=True, auto_now=False  )
	origin_of_the_courier = models.CharField(max_length=3000, blank=True,null=True)
	destination_of_the_courier = models.CharField(max_length=3000, blank=True,null=True)
	invoice_details = models.CharField(max_length=3000, blank=True,null=True)
	invoice_value = models.CharField(max_length=3000, blank=True,null=True) 
	airway_bill_number = models.CharField(max_length=3000, blank=False,null=False)
	general_description = models.CharField(max_length=3000, blank=True,null=True)
	number_of_packages = models.IntegerField()
	gross_weight = models.IntegerField()
	dimensonal_weight = models.IntegerField()


	def __str__(self):
		return self.senders_name
		
	def save(self, *args, **kwargs):
		super(InwardCourierRegistry, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural='InwardCourierRegistry'



