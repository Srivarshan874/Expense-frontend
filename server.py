#!/usr/bin/env python3
"""
Simple HTTP server for SpendWise Mobile Expense Tracker.
Runs locally on port 5173 or next available port.
"""
import http.server
import socketserver
import os
import sys

PORT = 5173
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers for PWA
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

def run():
    port = PORT
    for _ in range(10):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"🚀 SpendWise Mobile App running at: http://localhost:{port}")
                print(f"📁 Serving directory: {DIRECTORY}")
                httpd.serve_forever()
        except OSError:
            port += 1

if __name__ == "__main__":
    run()