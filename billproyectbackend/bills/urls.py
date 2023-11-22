from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductGenericView

router = DefaultRouter()
#Routes for Viewsets
router.register('product', ProductGenericView, basename = 'product')


urlpatterns = [
    path('', include(router.urls)),
]