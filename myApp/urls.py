from django.urls import path
from . import views GoogleCalendarInitView, GoogleCalendarRedirectView


urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='calendar-init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='calendar-redirect'),
]
