# CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
#!/usr/bin/env python3
"""
CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
Fennec Cameras - Zero-Dependency Local HTTP & MJPEG Stream Server

Built 100% with Python standard library (http.server, socket, json, urllib).
Requires ZERO external pip packages. Runs on any vanilla Linux machine, Raspberry Pi, or laptop.
"""

import os
import sys
import time
import json
import socket
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [HTTP-Core] %(message)s")


def find_conflict_free_port(preferred_port=8080, fallback_port=8081):
    """
    Conflict-Free Auto-Port Relocation Protocol.
    Checks if preferred_port (e.g., 8080) is used by Home Assistant / Plex,
    and automatically shifts to fallback_port (8081).
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        res = sock.connect_ex(('127.0.0.1', preferred_port))
        if res == 0:
            logging.info(f"Port {preferred_port} is occupied. Relocating server to fallback port {fallback_port}...")
            return fallback_port
        return preferred_port


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Threaded HTTP Server for concurrent camera streams & API requests."""
    daemon_threads = True


class FennecLocalAPIHandler(BaseHTTPRequestHandler):
    """Zero-dependency local HTTP API handler."""

    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Pure standard library system metrics
            status_payload = {
                "status": "online",
                "system": "Fennec Cameras Linux Core",
                "dependencies": "zero_external (python standard library)",
                "timestamp": int(time.time()),
                "nodes": [
                    {"id": "local-v4l2-webcam", "type": "USB Webcam", "status": "streaming"},
                    {"id": "android-node-01", "type": "Android Phone Node", "status": "active"}
                ]
            }
            self.wfile.write(json.dumps(status_payload, indent=2).encode('utf-8'))

        elif self.path == '/api/ping':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"PONG")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def log_message(self, format, *args):
        # Quiet default logging
        pass


def run_server():
    port = find_conflict_free_port(8080, 8081)
    server = ThreadedHTTPServer(('0.0.0.0', port), FennecLocalAPIHandler)
    logging.info(f"Starting Fennec Zero-Dependency API Server on http://0.0.0.0:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Shutting down HTTP server...")
        server.server_close()


if __name__ == '__main__':
    run_server()
