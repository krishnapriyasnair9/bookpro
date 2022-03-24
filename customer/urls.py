from django.urls import path
from customer import views
urlpatterns=[
    path("home",views.CustomerIndex.as_view(),name="custhome"),
    path("accounts/register",views.SignUp.as_view(),name="signup"),
    path("accounts/login",views.SignIn.as_view(),name="login"),
    path("accounts/logout",views.signout,name="signout"),
    path("accounts/password/reset",views.PasswordResetView.as_view(),name="passwordreset")
]