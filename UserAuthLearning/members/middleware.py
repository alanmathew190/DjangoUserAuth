import time
from datetime import datetime

class SimpleLoggingMiddleware:
    def __init__(self, get_response):
        # This runs only once when the server starts
        self.get_response = get_response

    def __call__(self, request):
        # This runs for every request

        start_time = time.time()  # record when request started

        print(f"[{datetime.now()}] Incoming {request.method} request to {request.path}")

        # Pass the request to the next middleware/view
        response = self.get_response(request)

        # Calculate how long the request took
        duration = time.time() - start_time
        print(f"--> Completed in {duration:.2f} seconds\n")

        # Return the response to the browser
        return response