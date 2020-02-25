from django.urls import path
from .views import HomePageView, Signup, GenerateRandomUserView, user_list

urlpatterns = [
    path('home', HomePageView.as_view(), name="home"),
    path("signup/", Signup, name="signup"),
    path("generate/", GenerateRandomUserView.as_view(), name="generate_name"),
    path("user_list_render/", user_list, name="users_list"),


]
