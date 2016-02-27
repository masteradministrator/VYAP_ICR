from rest_framework import serializers
from icr.models import InwardCourierRegistry

class InwardCourierRegistrySerializer(serializers.ModelSerializer):

	class Meta:
		model = InwardCourierRegistry
		fields = ('senders_code','senders_company','senders_address','senders_city','senders_name','senders_phoneno','senders_pincode','senders_state','senders_email','recivers_code','recivers_company','recivers_address','recivers_name','recivers_phoneno','recivers_pincode','recivers_state','recivers_email','special_instructions','service_sticker','original_senders_name','courier_service_used','courier_pickedup_by_name','pickup_empid','origin_of_the_courier','destination_of_the_courier','invoice_details','invoice_value','airway_bill_number','general_description','number_of_packages','gross_weight','dimensonal_weight')

