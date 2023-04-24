from django.urls import path
from . import views

urlpatterns = [
    path("friends/<int:pk>/", views.FriendsView.as_view()),
    path("friends/search/<int:pk>/", views.FriendsDetailView.as_view()),
]
