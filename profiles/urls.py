from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from profiles import views


router = SimpleRouter()
router.register('rest', views.ProfileViewset)

urlpatterns = router.urls