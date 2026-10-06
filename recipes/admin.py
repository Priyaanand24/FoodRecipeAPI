from django.contrib import admin

from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "cooking_time",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "ingredients",
    )

    ordering = (
        "-created_at",
    )