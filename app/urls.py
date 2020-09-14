from django.urls import path
from .views import HomePageView, Signup
urlpatterns = [
    path('home', HomePageView.as_view(), name="home"),
    path("signup/", Signup, name="signup"),


]
