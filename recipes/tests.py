from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Recipe


class RecipeAPITestCase(APITestCase):

    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Chicken Biryani",
            description="Indian rice dish",
            ingredients="Chicken, Rice, Spices",
            instructions="Cook everything together",
            cooking_time=60,
        )

        self.url = reverse("recipe-list")

    def test_create_recipe(self):
        data = {
            "name": "Pizza",
            "description": "Cheesy pizza",
            "ingredients": "Flour, Cheese, Tomato",
            "instructions": "Bake the pizza",
            "cooking_time": 30,
        }

        response = self.client.post(
            self.url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Recipe.objects.count(),
            2
        )

    def test_get_recipe_list(self):
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_recipe(self):
        url = reverse(
            "recipe-detail",
            kwargs={"pk": self.recipe.id}
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["name"],
            "Chicken Biryani"
        )

    def test_update_recipe(self):
        url = reverse(
            "recipe-detail",
            kwargs={"pk": self.recipe.id}
        )

        data = {
            "cooking_time": 90
        }

        response = self.client.patch(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.recipe.refresh_from_db()

        self.assertEqual(
            self.recipe.cooking_time,
            90
        )

    def test_delete_recipe(self):
        url = reverse(
            "recipe-detail",
            kwargs={"pk": self.recipe.id}
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Recipe.objects.count(),
            0
        )

    def test_invalid_cooking_time(self):
        data = {
            "name": "Bad Recipe",
            "description": "Invalid recipe",
            "ingredients": "Test",
            "instructions": "Test",
            "cooking_time": 0,
        }

        response = self.client.post(
            self.url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_duplicate_recipe_name(self):
        data = {
            "name": "Chicken Biryani",
            "description": "Duplicate",
            "ingredients": "Chicken",
            "instructions": "Cook",
            "cooking_time": 30,
        }

        response = self.client.post(
            self.url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )