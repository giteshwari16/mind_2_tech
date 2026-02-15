import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = "RapidRescue"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print("Opening in browser...")
        webbrowser.open(f"http://localhost:{PORT}/index.html")
        httpd.serve_forever()
except OSError as e:
    print(f"Error: {e}")
    print(f"Port {PORT} might be in use. Try closing other servers or restarting.")
