from django.conf.urls import url

from profile_tracking import views


urlpatterns = [
    url(r'^save/list/', views.ProfileSaveTrackingListView.as_view()),
]