# myproject/utils.py

from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.shortcuts import redirect

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):
        # Provide a custom response or redirect
        # For APIs, typically you would return a JSON response
        return Response({'detail': 'Authentication credentials were not provided.'}, status=401)

    return response
