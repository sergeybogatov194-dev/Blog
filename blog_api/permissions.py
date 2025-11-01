from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Только аутх. польз. могут видет представление списка
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение доступно для любого запроса
        # Поэтому всегда разрешаем запросы GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Права на запись разрешены только автору поста или админу
        return obj.author == request.user or request.user.is_staff