import logging
import time


class APIMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("api_performance")

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time

        if request.path.startswith("/api/"):
            self.logger.info(
                f"API {request.method} {request.path} - {response.status_code} - {duration:.3f}s"
            )

        return response
