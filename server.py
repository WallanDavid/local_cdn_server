    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "public, max-age=86400")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("X-CDN", "WallanCDN-Local")
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CDNHandler) as httpd:
        print(f"?? Servindo arquivos em http://localhost:{PORT}")
        httpd.serve_forever()
