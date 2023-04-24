from django.urls import path
from . import views

urlpatterns = [
    path("likes/", views.LikesView.as_view()),
    path("likes/<int:pk>/", views.LikesDetailView.as_view()),
]
