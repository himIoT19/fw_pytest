from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
from threading import Thread
import webbrowser
import socket
import time
import os

PORT_NUMBER = 8000


def start_localhost_server():
    """ Start the localhost server with specific port"""
    server_address = ('', PORT_NUMBER)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Running localhost on port: {PORT_NUMBER}")
    Thread(target=httpd.serve_forever).start()


def generate_free_port():
    """ Generate the unused port for localhost """
    sock = socket.socket()
    sock.bind(('', 0))
    global PORT_NUMBER
    PORT_NUMBER = sock.getsockname()[1]
    sock.close()


def check_index_html_file():
    """ Check whether index.html file is exists in the current directory """
    index_file = 'index.html'
    if not os.path.exists(index_file):
        input(f"{index_file} file not found in current directory. Enter to exit.")
        exit(1)
    return True


def main():
    check_index_html_file()
    generate_free_port()
    start_localhost_server()
    url = f'http://localhost:{PORT_NUMBER}'
    print(f'Opening report url {url} in default browser')
    time.sleep(1)
    webbrowser.open(url)


if __name__ == "__main__":
    main()
