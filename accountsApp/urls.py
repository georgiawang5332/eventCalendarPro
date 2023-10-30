from django.urls import path
from . import views

app_name = "accounts"

# Create your urls here.
urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),

]
