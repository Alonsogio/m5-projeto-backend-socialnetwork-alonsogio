from rest_framework import permissions
import pdb


class CheckIdOrNameIsDifferentFromYours(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == request.kwargs["pk"]:
            return False
        else:
            return True


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_authenticated
