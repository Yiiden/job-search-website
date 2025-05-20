from rest_framework import serializers
from .models import JobOpening, JobOpeningBenefit
from apps.companies.models import Company

class JobOpeningBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpeningBenefit
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name'] 

class JobOpeningSerializer(serializers.ModelSerializer):
    company = CompanySerializer()  # Nested serializer
    benefits = JobOpeningBenefitSerializer(many=True, read_only=True)

    class Meta:
        model = JobOpening
        fields = '__all__'

     