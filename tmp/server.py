from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print self.path
        print parse_qs(self.path[2:])
        self.wfile.write("<html><body><h1>Get Request Received!</h1></body></html>")
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        print form.getvalue("foo")
        print form.getvalue("bin")
        self.wfile.write("<html><body><h1>POST Request Received!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:8088...'
    httpd.serve_forever()

run()

#Test the HEADER, GET and POST requests using curl
#curl -I http://localhost:8088
#curl 'http://localhost:8088?foo=bar&bin=go'
#curl -d "foo=bar&bin=go" http://localhost:8088
