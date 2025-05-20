from rest_framework import serializers
from .models import Company, CompanyBenefit, StatutoryBenefit, OtherBenefit, Contact, CompanyWebsite, CompanyMedia, CompanyPhoto 

class StatutoryBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutoryBenefit
        fields = ['id', 'benefit']

class OtherBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherBenefit
        fields = ['id', 'benefit']

class CompanyBenefitSerializer(serializers.ModelSerializer):
    statutory = StatutoryBenefitSerializer(many=True, read_only=True)
    others = OtherBenefitSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyBenefit
        fields = ['id', 'benefits_description', 'statutory', 'others']

class CompanyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CompanyWebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyWebsite
        fields = '__all__'

class CompanyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPhoto
        fields = ['image']

class CompanyMediaSerializer(serializers.ModelSerializer):
    photos = CompanyPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = CompanyMedia
        fields = ['logo']

class CompanySerializer(serializers.ModelSerializer):
    benefits = CompanyBenefitSerializer(many=True, read_only=True)
    contacts = CompanyContactSerializer(many=True, read_only=True)
    websites = CompanyWebsiteSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = '__all__'