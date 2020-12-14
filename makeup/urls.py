from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'comments', CommentViewSet, basename='comment')
urlpatterns = router.urls
