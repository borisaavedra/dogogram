from django.contrib import admin
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):

    list_display = (
        "pk",
        "title",
        "user",
        "likes",
        "photo",
        "create_at",
        "modified_at"
    )

    list_display_links = (
        "pk",
        "title"
    )

    fieldsets = (
        (None, {
            "fields": (
                ("user", "profile"),
                ("title",),
                ("photo",),
                ("likes",),
                ("create_at", "modified_at")
            )
        }),
    )

    readonly_fields = ("thumbnail_preview", "create_at", "modified_at")

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
    