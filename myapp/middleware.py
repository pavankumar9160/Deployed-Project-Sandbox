# myproject/middleware.py

from django.shortcuts import redirect

class RedirectUnauthorizedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if response.status_code == 401 and not request.user.is_authenticated:
            # Redirect for non-API requests
            if 'application/json' not in request.META.get('HTTP_ACCEPT', ''):
                return redirect('/')
        
        return response
