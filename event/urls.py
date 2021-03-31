from django.urls import path
from . import views
from django.conf.urls import url
from event import views as core_views


urlpatterns = [
    path('', views.index, name = "index"),
    path('signup/', core_views.signup, name='signup'),
    path('events/', views.EventListView.as_view(), name="events"),
    path('event/<int:pk>', views.EventDetailView.as_view(), name="event-detail"),
    path('event/<int:pk>/update', views.EventUpdateView.as_view(), name="event-update"),
    path('event/<int:pk>/delete', views.EventDeleteView.as_view(), name="event-delete"),
    path('event/<int:pk>/eventattendence_create', views.EventAttendenceCreate.as_view(), name='add-attendence'),
    path('event/<int:pk>/event_attendence_list', views.EventAttendenceListView.as_view(), name='attendence-list'),
    path('event/event_attendence_detail/<int:pk>', views.EventAttendenceDetailView.as_view(), name='attendence-detail')
]

# from django.conf.urls import url
# from event import views as core_views

# urlpatterns = [
#     url(r'^signup/$', core_views.signup, name='signup'),
# ]