from rest_framework import permissions


class CreateOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == "create"
