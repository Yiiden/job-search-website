from rest_framework.routers import DefaultRouter
from apps.jobs.views import JobOpeningViewSet

router = DefaultRouter()
router.register(r'', JobOpeningViewSet, basename='job')  # 不加 'jobs'
urlpatterns = router.urls