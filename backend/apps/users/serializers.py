from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, ValidationError

# 註冊用
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})  # 新增確認密碼欄位
    password = serializers.CharField(write_only=True,style={'input_type': 'password'})  # 設定為密碼輸入框)
    email = serializers.EmailField(required=True, allow_blank=False)  # 設定為必填欄位
    username = serializers.CharField(required=True, allow_blank=False)  # 設定為必填欄位
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'email': {'required': True, 'allow_blank': False}}

    def validate(self, data):
        # 檢查密碼與確認密碼是否一致
        if data['password'] != data['confirm_password']:
            raise ValidationError({"password": "密碼與確認密碼不一致"})
        return data

    def create(self, validated_data):
        # 移除 confirm_password，因為它不需要存入資料庫
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# 自訂 Token 取得 serializer（可自定回傳內容）
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'username': self.user.username})
        return data