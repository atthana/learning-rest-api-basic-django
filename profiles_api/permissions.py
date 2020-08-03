# Make permission in Django otherwise any users can edit in others.
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: # ให้เปลี่ยนค่าได้แค่ user ตัวเองเท่านั้น
            return True

        return obj.id == request.user.id