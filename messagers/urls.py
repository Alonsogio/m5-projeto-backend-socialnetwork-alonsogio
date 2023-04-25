from django.urls import path
from messagers import views

urlpatterns = [
    path("messages/<int:pk>/", views.MessagesView.as_view()),
]
