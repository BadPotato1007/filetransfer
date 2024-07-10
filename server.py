import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

class CustomHandler(Handler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
