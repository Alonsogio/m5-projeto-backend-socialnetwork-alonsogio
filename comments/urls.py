from django.urls import path
from . import views

urlpatterns = [
    path("likes/", views.CommentsView.as_view()),
    path("likes/<int:pk>/", views.CommentsDetailView.as_view()),
]
