import http.server
import socketserver

# Set the port number you want to use for the local server
PORT = 8000

# Change directory to the folder where your HTML file is located
web_dir = "./index.html"
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server started at port {PORT}")
    httpd.serve_forever()
