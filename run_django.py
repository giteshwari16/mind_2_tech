import http.server
import socketserver
import webbrowser
import os
import subprocess
import threading
import time
import sys

PORT_FRONTEND = 8000
PORT_BACKEND = 8001
DIRECTORY = "RapidRescue"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_django_backend():
    """Start Django backend server"""
    try:
        print("Starting Django backend server...")
        subprocess.run([
            sys.executable, "manage.py", "runserver", f"127.0.0.1:{PORT_BACKEND}"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting Django backend: {e}")
    except KeyboardInterrupt:
        print("\nDjango backend server stopped.")

def start_frontend():
    """Start frontend server"""
    try:
        with socketserver.TCPServer(("", PORT_FRONTEND), Handler) as httpd:
            print(f"Frontend server running at http://localhost:{PORT_FRONTEND}")
            print(f"Backend API running at http://localhost:{PORT_BACKEND}/api/")
            print("Opening in browser...")
            webbrowser.open(f"http://localhost:{PORT_FRONTEND}/index.html")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}")
        print(f"Port {PORT_FRONTEND} might be in use. Try closing other servers or restarting.")
    except KeyboardInterrupt:
        print("\nFrontend server stopped.")

def main():
    print("🚀 Starting RapidRescue Application...")
    print("=" * 50)
    
    # Check if requirements are installed
    try:
        import django
        import rest_framework
        import corsheaders
        print("✓ Django dependencies found")
    except ImportError:
        print("⚠️  Django dependencies not found. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
            print("✓ Dependencies installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies. Please run: pip install -r requirements.txt")
            return
    
    # Run database migrations
    try:
        print("🔄 Running database migrations...")
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True, capture_output=True)
        print("✓ Database migrations completed")
    except subprocess.CalledProcessError:
        print("⚠️  Migration failed or already completed")
    
    # Start Django backend in a separate thread
    backend_thread = threading.Thread(target=start_django_backend, daemon=True)
    backend_thread.start()
    
    # Give backend time to start
    time.sleep(2)
    
    # Start frontend in main thread
    try:
        start_frontend()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down RapidRescue...")
        sys.exit(0)

if __name__ == "__main__":
    main()
