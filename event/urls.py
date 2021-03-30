from django.urls import path
from . import views
from django.conf.urls import url
from event import views as core_views


urlpatterns = [
    path('', views.index, name = "index"),
    path('signup/', core_views.signup, name='signup'),
    path('events/', views.EventListView.as_view(), name="events"),
    path('event/<int:pk>', views.EventDetailView.as_view(), name="event-detail"),
    path('event/<int:pk>/eventattendence_create', views.EventAttendenceCreate.as_view(), name='add-attendence'),
    path('event/<int:event_id>/eventattendence_detail/<int:eventattendence_id>', views.EventAttendenceDetail.as_view(), name='attendence-detail'),
]

# from django.conf.urls import url
# from event import views as core_views

# urlpatterns = [
#     url(r'^signup/$', core_views.signup, name='signup'),
# ]