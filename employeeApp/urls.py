from django.urls import path
from . import views

app_name = "emp"

# Create your urls here.
urlpatterns = [
    path("employee/", views.AllEmployeeListView.as_view(), name="employee"),

]
