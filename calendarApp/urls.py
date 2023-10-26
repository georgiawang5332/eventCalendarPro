from django.urls import path
from . import views

app_name = "calendarapp"

# Create your urls here.
urlpatterns = [
    path("calender/", views.AllCalendarListView.as_view(), name="calendar"),

]
