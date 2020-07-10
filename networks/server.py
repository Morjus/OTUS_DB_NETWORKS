import socket
import json


class Server:
    def __init__(self):
        self.sock = socket.socket()
        self.HOST = socket.gethostname()
        self.PORT = 8889
        self.conn = None
        self.addr = None
        self.data = None

    def server(self):
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(10)
        self.conn, self.addr = self.sock.accept()

    def get_data(self):
        self.data = self.conn.recv(1024)
        print("Got data", self.data)

    def make_headers_json(self):
        data = self.data.decode("utf-8").split('\r\n')
        res = {}
        for line in data:
            if "HTTP" in line or line == "":
                pass
            else:
                splitted = line.split(": ")
                res[splitted[0]] = splitted[1]
        return res

    def send_data(self):
        res = self.make_headers_json()
        self.conn.send(f'HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: '
                       f'json\n\n{json.dumps(res)}'.encode("utf-8"))
        self.sock.close()
        return True


if __name__ == "__main__":
    while True:
        s = Server()
        s.server()
        s.get_data()
        if s.send_data():
            break
