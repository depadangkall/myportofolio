from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change experiences."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "Only the portfolio owner can create or delete data, and editors can only update it."
    editor_permission = None

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return request.method in ("PUT", "PATCH") and self.is_editor(request.user)

    def is_editor(self, user):
        if self.editor_permission:
            return user.has_perm(self.editor_permission)
        return user.groups.filter(name="Editor").exists()


class IsSkillOwnerOrEditorOrReadOnly(IsPortfolioOwnerOrEditorOrReadOnly):
    editor_permission = "main.change_skill"
