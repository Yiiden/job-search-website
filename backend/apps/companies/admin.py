from django.contrib import admin

from .models import Company, CompanyBenefit, StatutoryBenefit, OtherBenefit, Contact, CompanyWebsite, CompanyMedia, CompanyPhoto
# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyBenefit)
admin.site.register(StatutoryBenefit)
admin.site.register(OtherBenefit)
admin.site.register(Contact)
admin.site.register(CompanyWebsite)
admin.site.register(CompanyMedia)
admin.site.register(CompanyPhoto)