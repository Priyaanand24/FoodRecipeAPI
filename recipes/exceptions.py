import logging

from rest_framework.views import exception_handler


logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "success": False,
            "status_code": response.status_code,
            "errors": response.data,
        }

        return response

    logger.exception(
        "Unhandled exception in API",
        exc_info=exc
    )

    return None