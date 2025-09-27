import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from etl.parse_xml import parse_sms

# Load transactions from XML
transactions = parse_sms("data/raw/modified_sms_v2.xml")

# Helper function to find a transaction by ID
def get_transaction(txn_id):
    for txn in transactions:
        if txn["id"] == txn_id:
            return txn
    return None

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path).path
        parts = parsed_path.strip("/").split("/")

        if parsed_path == "/transactions":
            self._set_headers()
            self.wfile.write(json.dumps(transactions).encode())
        elif len(parts) == 2 and parts[0] == "transactions":
            txn = get_transaction(parts[1])
            if txn:
                self._set_headers()
                self.wfile.write(json.dumps(txn).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())

    def do_POST(self):
        if self.path != "/transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())
            return

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
            transactions.append(data)
            self._set_headers(201)
            self.wfile.write(json.dumps({"message": "Transaction added"}).encode())
        except Exception as e:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_PUT(self):
        parts = self.path.strip("/").split("/")
        if len(parts) != 2 or parts[0] != "transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())
            return

        txn = get_transaction(parts[1])
        if not txn:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
            return

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
            txn.update(data)
            self._set_headers(200)
            self.wfile.write(json.dumps({"message": "Transaction updated"}).encode())
        except Exception as e:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_DELETE(self):
        parts = self.path.strip("/").split("/")
        if len(parts) != 2 or parts[0] != "transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())
            return

        txn = get_transaction(parts[1])
        if not txn:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
            return

        transactions.remove(txn)
        self._set_headers(200)
        self.wfile.write(json.dumps({"message": "Transaction deleted"}).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
