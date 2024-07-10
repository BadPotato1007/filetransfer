import http.server
import socketserver
import os
import json

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/files':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            self.wfile.write(json.dumps(files).encode())
        else:
            if self.path == '/':
                self.path = '/index.html'
            return super().do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
