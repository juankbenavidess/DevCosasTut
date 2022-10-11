"""User permission classes"""

from rest_framework.permissions import BasePermission

from users.models import User


class IsStandarduser(BasePermission):
    """Allow access to create experience, exrtas and proyects"""

    def has_permission(self, request, view):
        try:
            user = User.objects.get(
                email=request.user,
                is_recruiter=False
            )
            #return not user.is_recruiter
        except User.DoesNotExist:
            return False
        return True
