from datetime import datetime
import logging

# Configure logging to write to a file
logging.basicConfig(
    filename='requests.log',  # log file name
    level=logging.INFO,
    format='%(message)s'
)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user info
        user = request.user if request.user.is_authenticated else "Anonymous"

        # Log request details
        logging.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        # Continue processing request
        response = self.get_response(request)
        return response
