from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    bg_color_hex = models.CharField(max_length=7)  # 例如 "#FFFFFF"
    industry = models.CharField(max_length=100)
    industry_description = models.TextField()
    main_product = models.CharField(max_length=200)
    capital = models.IntegerField()
    employees = models.IntegerField()
    address = models.CharField(max_length=255)
    introduction = models.TextField()
    
    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
    
class CompanyBenefit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='benefits')
    benefits_description = models.TextField()

    def __str__(self):
        return f"{self.company.name} 福利"
    
class StatutoryBenefit(models.Model):
    benefit_group = models.ForeignKey(CompanyBenefit, on_delete=models.CASCADE, related_name='statutory')
    benefit = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.benefit_group.company.name} 法定福利： {self.benefit}"
    

class OtherBenefit(models.Model):
    benefit_group = models.ForeignKey(CompanyBenefit, on_delete=models.CASCADE, related_name='others')
    benefit = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.benefit_group.company.name} 其他福利： {self.benefit}"
    
class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)  # 聯絡人姓名
    email = models.EmailField()  # 聯絡人電子郵件
    phone = models.CharField(max_length=20)  # 聯絡人電話
    fax = models.CharField(max_length=20, blank=True, null=True)  # 聯絡人傳真

    def __str__(self):
        return f"{self.company.name} 聯絡人"   

class CompanyWebsite(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='websites')
    website = models.URLField()

    def __str__(self):
        return f"{self.company.name} 相關連結"
    
class CompanyMedia(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='media')
    logo = models.FileField(upload_to='company_logo/')

    def __str__(self):
        return f"{self.company.name} Media"

class CompanyPhoto(models.Model):
    media = models.ForeignKey(CompanyMedia, on_delete=models.CASCADE, related_name='photos')
    photo = models.FileField(upload_to='company_photo/')

    def __str__(self):
        return f"{self.media.company.name} 公司圖片"