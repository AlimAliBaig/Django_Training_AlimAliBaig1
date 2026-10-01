from django.urls import path
from .views import (
    UserLoginView,
    UserLogoutView,
    dashboard,
    home,
    quiz_page,
    signup_view,
    submit_quiz,
)

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup_view, name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("quiz/<int:quiz_id>/", quiz_page, name="quiz_page"),
    path("quiz/<int:quiz_id>/submit/", submit_quiz, name="submit_quiz"),
]
