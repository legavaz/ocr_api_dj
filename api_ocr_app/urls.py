from rest_framework import routers
from .api import Source_tableViewSet

router = routers.DefaultRouter()
router.register('api/Source_table', Source_tableViewSet, 'source_table')


urlpatterns = router.urls