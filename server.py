#!/usr/bin/env python3
"""
Simple HTTP server for Music Practice Suite
Serves files on localhost:8003
"""

import http.server
import socketserver
import os
import sys

PORT = 8004

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # Disable caching for development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🎵 Music Practice Suite Server")
        print(f"📍 Serving at: http://localhost:{PORT}")
        print(f"📁 Directory: {os.getcwd()}")
        print(f"🔗 Main page: http://localhost:{PORT}")
        print(f"🎼 Lines (Bebop): http://localhost:{PORT}/lines.html")
        print(f"🎹 Voicings (Chords): http://localhost:{PORT}/Chord%20Practice%20Program/")
        print(f"\n⚡ Press Ctrl+C to stop the server")
        print("-" * 60)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped.")
            sys.exit(0)

if __name__ == "__main__":
    main()

