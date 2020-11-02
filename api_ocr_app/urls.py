from rest_framework import routers
from .api import Source_tableViewSet, TestView

router = routers.DefaultRouter()
router.register('api/Source_table', Source_tableViewSet, 'source_table')
router.register('api/test', TestView, 'TestView')


urlpatterns = router.urls

# print('debugg', router)