from django.contrib.auth.models import User 
from django.contrib import admin
from users.models import Profile, FollowingFollowers
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserFollowInline(admin.StackedInline):
    model = FollowingFollowers
    fk_name = "following_user"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    
    # Columnas en la lista de usuarios en el admin
    list_display = ("pk", "user","phone_number", "website", "picture", "create_at") 

    # Las columnas que sean link y lleven al detalle del registro
    list_display_links = ("pk", "user")

    # La columnas que se directamnte editables desde la tabla 
    list_editable = ("phone_number", "website", "picture")

    # Campo de busqueda de en el admin del modelo
    search_fields = ("user__email", "user__first_name", "user__last_name", "website")

    # Filtros por que los que se filtrar la tabla del modelo
    list_filter = ("create_at", "modified_at", "user__is_active", "user__is_staff")

    # Campos en el detalle de cada registro del modelo
    fieldsets = (
        ("Profile", {
            "fields": (("user", "picture"),)
        }),
        ("Extra info", {
            "fields": (
                ("website", "phone_number"),
                ("bio")
            )
        }),
        ("Metadata", {
            "fields": (
                ("create_at", "modified_at"),
            )
        })
    )

    # Campos de solo lectura
    readonly_fields = ("create_at", "modified_at")



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"


class UserAdmin(BaseUserAdmin):
    
    inlines = (ProfileInline,)
    inlines = (UserFollowInline,)
    
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff"
    )

    fieldsets = (
        ("Followers", {
            "fields": (
                ("followers", ),
            )
        }),
    )

    list_editable = ("is_active",)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)