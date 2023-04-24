from rest_framework import permissions
from .models import Follower
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_authenticated
