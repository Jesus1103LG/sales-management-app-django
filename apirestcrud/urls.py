from rest_framework import routers
from .api import ProductViewSet, SaleViewSet, IncomeViewSet

router = routers.DefaultRouter()

router.register('products',ProductViewSet,'products')
router.register('sales',SaleViewSet,'sales')
router.register('incomes',IncomeViewSet,'incomes')

urlpatterns = router.urls