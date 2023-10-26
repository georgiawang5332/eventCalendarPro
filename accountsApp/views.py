from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accountsApp.forms import SignInForm, SignUpForm

# Create your views here.
# 登入
class SignInView(View):
    """ User signin view """

    template_name = "accounts/signin.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("calendarapp:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)

# 登出
def signout(request):
    """ User signout view """

    logout(request)
    return redirect("acc:signin")

# 註冊
class SignUpView(View):
    """ User signup/registration(登記) view """

    template_name = "accounts/signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("acc:signin")
        context = {"form": forms}
        return render(request, self.template_name, context)