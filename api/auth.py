import base64

# Hardcoded credentials for demonstration
USERNAME = "admin"
PASSWORD = "password"

def check_auth(headers):
    """
    Check the Authorization header for valid Basic Auth credentials.
    """
    auth_header = headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Basic '):
        return False

    encoded = auth_header.split(' ')[1]
    try:
        decoded = base64.b64decode(encoded).decode()
        username, password = decoded.split(':', 1)
        return username == USERNAME and password == PASSWORD
    except Exception:
        return False

def require_auth(handler):
    """
    Enforce authentication for a request.
    Returns True if authorized, otherwise sends 401 response.
    """
    if not check_auth(handler.headers):
        handler.send_response(401)
        handler.send_header('WWW-Authenticate', 'Basic realm="Access to transactions"')
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(b'{"error": "Unauthorized"}')
        return False
    return True
