from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductGenericView, BillGenericView, SellDetailGenericView

router = DefaultRouter()
#Routes for Viewsets
router.register('product', ProductGenericView, basename = 'product')
router.register('bill', BillGenericView, basename = 'bill')
router.register('billdetail', SellDetailGenericView, basename = 'billdetail')



urlpatterns = [
    path('', include(router.urls)),
]