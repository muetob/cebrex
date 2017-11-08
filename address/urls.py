from django.conf.urls import url

from address import views


urlpatterns = [
    url(r'^list/', views.AddressListView.as_view()),
]