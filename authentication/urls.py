from authentication.views import EmailValidationView, RegistrationView, UsernameValidationView,VerificationView, LoginView,LogoutView,profile
from django.urls import path
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.urls import reverse_lazy

app_name = "authentication"
urlpatterns= [
    path('register/',(RegistrationView.as_view()), name="register"),
    path('login/',(LoginView.as_view()), name="login"),
    path('logout/',(LogoutView.as_view()), name="logout"),
    path('validate-username/',csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email/',csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
    path('activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),
    path("profile/",profile,name="profile"),
    
]


