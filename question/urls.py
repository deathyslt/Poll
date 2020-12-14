from django.urls import path

from .views import signup_account, login_account, home

urlpatterns = [
    path('signup/', signup_account, name='signup'),
    path('login/', login_account, name='login'),
    path('home/', home, name='home')
]
