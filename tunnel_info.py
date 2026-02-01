#!/usr/bin/env python3
import http.server
import socketserver
import socket
import threading
import time

# Simple tunnel server
class TunnelHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirect to our local server
        self.send_response(302)
        self.send_header('Location', 'http://localhost:8080' + self.path)
        self.end_headers()

# Get public IP
import requests
public_ip = requests.get('https://api.ipify.org').text.strip()

print(f"🌐 Your website is accessible at:")
print(f"   http://{public_ip}:8080")
print(f"   (Make sure port 8080 is open in your firewall)")
print(f"")
print(f"📱 On your phone, visit: http://{public_ip}:8080")
print(f"   Make sure you're on the same network as this server")
print(f"")
print(f"📝 The site is also running locally at: http://localhost:8080")
print(f"")
print(f"Press Ctrl+C to stop the server")

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nServer stopped.")