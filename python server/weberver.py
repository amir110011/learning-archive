from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.path[1:].encode())


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), EchoHandler)
    print('server runing oon port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
