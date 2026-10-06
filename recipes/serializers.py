from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "description",
            "ingredients",
            "instructions",
            "cooking_time",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_name(self, value):
        value = value.strip()

        if len(value) < 2:
            raise serializers.ValidationError(
                "Recipe name must contain at least 2 characters."
            )

        return value

    def validate_cooking_time(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Cooking time must be greater than 0 minutes."
            )

        return value