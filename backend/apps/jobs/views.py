from django.shortcuts import render
from rest_framework import viewsets
from .models import JobOpening
from .serializers import JobOpeningSerializer
# Create your views here.

class JobOpeningViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing and editing job openings.
    """
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer