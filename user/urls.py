from django.urls import path
from .views import LoginView, UserRegister, LogoutView
from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage/index.html'), name='logout'),#template_name="polls/login.html"
]
