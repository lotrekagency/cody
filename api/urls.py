from rest_framework import routers

from .views import ProjectsViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectsViewSet, basename='projects')

urlpatterns = router.urls
