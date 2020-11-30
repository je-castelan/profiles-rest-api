from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # If method is safeful (GET)
        if request.method in permissions.SAFE_METHODS:
            return True
        # If not safeful, it must check if the method is executed by the same user.
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        return obj.user_profile.id == request.user.id or request.method in permissions.SAFE_METHODS