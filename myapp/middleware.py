# myapp/middleware.py

class MyCustomMiddleware:
    def __init__(self, get_response):
        print("middleware_init")
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("middleware_call")
        response = self.get_response(request)
        print("response",response)
        # Code to be executed for each request/response after
        # the view is called.

        return response
