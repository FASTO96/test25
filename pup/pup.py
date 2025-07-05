from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'hi py the projct')

if __name__ == '__main__':
    server_address = ('', 80)
    httpd = HTTPServer(server_address, SimpleHandler)
    print('Serving on port 80...')
    httpd.serve_forever()
