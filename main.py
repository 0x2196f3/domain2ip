import base64
import http.server
import urllib.request
import urllib.parse

import node
import server

PORT = 8000


class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path[1:]
        print(path)
        ipv4 = True
        ipv6 = True

        # Extract query arguments
        query_args = urllib.parse.parse_qs(self.path.split('?')[1]) if '?' in self.path else {}
        if 'ipv4' in query_args:
            ipv4 = query_args['ipv4'][0].lower() == 'true'
        if 'ipv6' in query_args:
            ipv6 = query_args['ipv6'][0].lower() == 'true'

        if path.startswith("http"):
            links = server.get_links(path)
            new_links = []
            for link in links:
                # print(link)
                new_links += node.replace_domain2ip(link, ipv4, ipv6)
                # print(new_links)

            new_url = server.build_url(path, new_links)
            req = urllib.request.Request(new_url)
            with urllib.request.urlopen(req) as response:
                self.send_response(response.getcode())
                for key, value in response.info().items():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        else:
            link = path
            new_links = node.replace_domain2ip(link, ipv4, ipv6)
            response = "\n".join(new_links)
            # print(response)
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(base64.b64encode(response.encode()))


def run_server():
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, ProxyHandler)
    print(f"Starting server on port {PORT}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
