
import config

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((config.SERVER_DATA_HOST, config.SERVER_DATA_PORT), Handler)

print("serving at port", config.SERVER_DATA_PORT)
httpd.serve_forever()
