from django.shortcuts import render
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer

# Create your views here.

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer