import http.server
import json
import sys

PORT = 8080 # Match the port in your ~/.canonic/api.lock for testing

class MockCanonicHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True, "version": "1.0.0-mock"}).encode())

    def do_POST(self):
        if self.path == '/session/start':
            length = int(self.headers['Content-Length'])
            body = json.loads(self.rfile.read(length))
            print(f"\n[Mock] Received /session/start:")
            print(json.dumps(body, indent=2))
            
            # Simulate Canonic response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True, "sessionId": "mock-session-123"}).encode())
            
            # After sending response, simulate user clicking "Implement this"
            # by sending a POST back to the agent's callbackUrl
            callback_url = body.get('callbackUrl')
            if callback_url:
                print(f"\n[Mock] Simulating user response to {callback_url}...")
                import urllib.request
                response_data = {
                    "sessionId": "mock-session-123",
                    "file": body.get('file'),
                    "content": "# Mock Edited Content\nThis was edited in mock Canonic.",
                    "prompt": "Implement this"
                }
                req = urllib.request.Request(
                    callback_url, 
                    data=json.dumps(response_data).encode(),
                    headers={'Content-Type': 'application/json'}
                )
                try:
                    with urllib.request.urlopen(req) as f:
                        print(f"[Mock] Agent received response: {f.status}")
                except Exception as e:
                    print(f"[Mock] Failed to send callback: {e}")

if __name__ == '__main__':
    print(f"Starting Mock Canonic API on port {PORT}...")
    http.server.HTTPServer(('127.0.0.1', PORT), MockCanonicHandler).serve_forever()
