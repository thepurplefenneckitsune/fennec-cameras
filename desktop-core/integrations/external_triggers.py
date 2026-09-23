# CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
#!/usr/bin/env python3
"""
CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
Fennec Cameras - External Sensor Webhook & Hardware Trigger Listener

Built 100% with Python standard library (http.server, json, time).
Zero external dependencies required.
Receives external triggers from Zigbee / Z-Wave / Wi-Fi door sensors or PIR detectors to start recording.
"""

import json
import time
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [Sensor-Trigger] %(message)s")


class SensorTriggerWebhookHandler(BaseHTTPRequestHandler):
    """Listens for HTTP POST webhook triggers from Zigbee / Z-Wave / Home Assistant automation rules."""

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            payload = json.loads(post_data.decode('utf-8'))
            sensor_name = payload.get("sensor", "unknown_zigbee_sensor")
            action = payload.get("action", "motion")
            camera_id = payload.get("target_camera", "camera-01")

            logging.info(f"RECEIVED HARDWARE TRIGGER: [{sensor_name}] -> Action: [{action}] -> Target: [{camera_id}]")
            
            # Concept response: Trigger 30-second ring-buffer recording
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            response_payload = {
                "status": "recording_triggered",
                "camera_id": camera_id,
                "duration_sec": 30,
                "timestamp": int(time.time())
            }
            self.wfile.write(json.dumps(response_payload).encode('utf-8'))

        except Exception as e:
            logging.error(f"Error parsing sensor webhook payload: {e}")
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"400 Bad Request")

    def log_message(self, format, *args):
        pass


def run_trigger_listener(port=8082):
    server = HTTPServer(('0.0.0.0', port), SensorTriggerWebhookHandler)
    logging.info(f"Starting Sensor Trigger Webhook Listener on http://0.0.0.0:{port}/trigger")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    run_trigger_listener()
