from rest_framework import permissions

class IsAdminOrSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is an admin or superadmin.
        return request.user and (request.user.is_staff or request.user.is_superuser)
