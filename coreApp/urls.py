from django.urls import path
from . import views

app_name = "core"

# Create your urls here.
urlpatterns = [
    path("core/", views.AllCoreListView.as_view(), name="core"),

]
