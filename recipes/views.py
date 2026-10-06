import logging

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Recipe
from .serializers import RecipeSerializer


logger = logging.getLogger(__name__)

permission_classes = [AllowAny]
class RecipeViewSet(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        logger.info("Fetching recipe list")

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info(
            "Fetching recipe with id=%s",
            kwargs.get("pk")
        )

        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info(
            "Creating recipe: %s",
            request.data.get("name")
        )

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info(
            "Updating recipe with id=%s",
            kwargs.get("pk")
        )

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.info(
            "Deleting recipe with id=%s",
            kwargs.get("pk")
        )

        return super().destroy(request, *args, **kwargs)