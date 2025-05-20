from rest_framework.routers import DefaultRouter
from apps.companies.views import CompanyViewSet

router = DefaultRouter()
router.register(r'', CompanyViewSet, basename='company')  # 不加 'companies'

urlpatterns = router.urls  