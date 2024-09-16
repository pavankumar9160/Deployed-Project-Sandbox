# exceptions.py

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.utils import json

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):
        # Add a custom message or handle redirection
        response = Response(
            data={"detail": "Authentication failed. Redirecting to home."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    return response
