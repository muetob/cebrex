from django.conf.urls import url

from profiles import views


urlpatterns = [
    url(r'^list/', views.ProfileViewset),
    # url(r'^detail/(?P<pk>[0-9]+)/$', views.ProfileViewset.as_view()),
    # url(r'^update/(?P<pk>[0-9]+)/$', views.ProfileViewset.as_view())
]