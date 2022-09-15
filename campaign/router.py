from camrecomend.viewsets import TestViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('test',TestViewset)


