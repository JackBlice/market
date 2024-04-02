from products.views import ProductModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', ProductModelViewSet, basename='user')
urlpatterns = router.urls