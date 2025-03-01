# advanced_features_and_security/admin.py

from django.contrib import admin
from .models import Book, CustomUser, Article
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns in the list view
    search_fields = ("title", "author")  # Enables searching by title and author
    list_filter = ("publication_year",)  # Filters by publication year


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "date_of_birth", "profile_photo", "password1", "password2"),
        }),
    )

    search_fields = ("email", "username")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)


# ✅ Ensure Permissions Exist Before Assigning Them
def setup_groups():
    content_type = ContentType.objects.get_for_model(Article)

    # List of required permissions
    permission_codenames = ["can_view", "can_create", "can_edit", "can_delete"]

    # Ensure all permissions exist
    existing_codenames = set(
        Permission.objects.filter(content_type=content_type)
        .values_list("codename", flat=True)
    )

    for codename in permission_codenames:
        if codename not in existing_codenames:
            Permission.objects.create(
                codename=codename,
                name=f"Can {codename.split('_')[1]} articles",
                content_type=content_type,
            )

    # Fetch permissions after creating any missing ones
    permissions = Permission.objects.filter(content_type=content_type, codename__in=permission_codenames)

    # Create or get groups
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions to groups
    editors.permissions.set(permissions.filter(codename__in=["can_view", "can_create", "can_edit"]))
    viewers.permissions.set(permissions.filter(codename="can_view"))
    admins.permissions.set(permissions)


# ✅ Ensure setup_groups runs only after migrations are applied
def run_after_migrations():
    from django.db.utils import OperationalError, ProgrammingError

    try:
        setup_groups()
    except (OperationalError, ProgrammingError):
        # Prevent errors if migrations haven't been run yet
        pass


run_after_migrations()


