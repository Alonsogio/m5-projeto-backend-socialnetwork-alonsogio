from django.urls import path
from . import views

urlpatterns = [
    path("followers/<int:pk>/", views.FollowersView.as_view()),
    path("followers/unfollow/<int:pk>/", views.FollowersDetailView.as_view()),
]
