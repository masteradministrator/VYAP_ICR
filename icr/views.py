import csv
from django.utils import timezone
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status, generics, views
from rest_framework.permissions import BasePermission
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

from icr.models import InwardCourierRegistry
from icr.serializers import InwardCourierRegistrySerializer


class InwardCourierRegistryView(views.APIView):
    queryset = InwardCourierRegistry.objects.all()
    serializer_class = InwardCourierRegistrySerializer

    def post(self, request, *args, **kwargs):
        print('This is a POST req')
        serializer = InwardCourierRegistrySerializer(data=request.data)
        if serializer.is_valid():
        	instance = serializer.save()
        return HttpResponse('This is POST request222')

    def perform_create(self, serializer):
        print('trace')
        instance = serializer.save()


class InwardCourierRegistryViewSet(viewsets.ModelViewSet):
    queryset = InwardCourierRegistry.objects.all()
    serializer_class = InwardCourierRegistrySerializer

