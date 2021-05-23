from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Владелец или администратор
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверка прав доступа
        """
        user_email = obj.owner.email
        is_self = str(user_email) == str(request.user)
        is_admin = bool(request.user and request.user.is_staff)
        return is_self or is_admin

class IsAdminOrLeader(BasePermission):
    """
    Владелец или администратор
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверка прав доступа
        """
        is_admin = bool(request.user and request.user.is_staff)
        print(request.user.is_leader)
        is_leader = request.user.is_leader
        return  is_admin or is_leader
