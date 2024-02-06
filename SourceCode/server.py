import http.server
import webbrowser

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    address = ('localhost', 8000)
    server = http.server.HTTPServer(address, MyHTTPRequestHandler)
    webbrowser.open("http://localhost:8000/leaderboard.html")
    server.serve_forever()