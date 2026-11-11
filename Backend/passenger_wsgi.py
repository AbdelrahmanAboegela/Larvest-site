import sys
import os
import traceback

# ── 1. Add virtualenv site-packages to sys.path ──────────────────────────────
# Guarantees Python imports (django, rest_framework, etc.) work even if Passenger starts with system python
VENV_PACKAGES = '/home/byxtwipq/virtualenv/larvest_backend/3.10/lib/python3.10/site-packages'
if os.path.exists(VENV_PACKAGES) and VENV_PACKAGES not in sys.path:
    sys.path.insert(0, VENV_PACKAGES)

APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

# ── 2. Point Django at the correct settings module ───────────────────────────
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agrisens.settings')

# ── 3. Expose the WSGI application with error reporting fallback ──────────────
try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception:
    # Diagnostic fallback: If Django fails to initialize, renders the exact traceback in the browser
    error_traceback = traceback.format_exc()
    
    def application(environ, start_response):
        status = '500 Internal Server Error'
        output = f"""<!DOCTYPE html>
<html>
<head><title>Django WSGI Startup Error</title></head>
<body style="font-family: monospace; padding: 20px; background: #1e1e1e; color: #ff6b6b;">
  <h2>⚠️ Django Startup Exception (500 Error Diagnostic)</h2>
  <pre style="background: #2d2d2d; color: #f8f8f2; padding: 15px; border-radius: 5px; overflow-x: auto;">{error_traceback}</pre>
</body>
</html>""".encode('utf-8')
        response_headers = [('Content-Type', 'text/html; charset=utf-8'), ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output]
