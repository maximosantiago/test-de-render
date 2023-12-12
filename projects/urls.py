from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() #defaultRouter crea el CRUD

router.register("api/projects", ProjectViewSet, b"Projects")

urlpatterns = router.urls