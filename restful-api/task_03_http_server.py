#!/usr/bin/python3
"""A simple API built with http.server that serves text and JSON data."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handles incoming HTTP requests and routes them by their path."""

    def send_text(self, status_code, message):
        """Send a plain text response with the given status code."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def send_json(self, status_code, data):
        """Send a dictionary as a JSON response with the given status code."""
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """Respond to GET requests based on the endpoint requested."""
        if self.path == "/":
            self.send_text(200, "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_json(200, data)

        elif self.path == "/status":
            self.send_text(200, "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_json(200, info)

        else:
            self.send_text(404, "Endpoint not found")


def run(port=8000):
    """Start the HTTP server on the given port and serve until stopped."""
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Serving on http://localhost:{}".format(port))
    httpd.serve_forever()


if __name__ == "__main__":
    run()