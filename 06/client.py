import socket
import threading


class Client:
    def __init__(self, server_address, url_file, num_threads):
        self.server_address = server_address
        self.url_file = url_file
        self.num_threads = num_threads

    def send_request(self, url):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect(self.server_address)
            client_socket.send(url.encode())

            response = client_socket.recv(1024).decode()

            print(f"{url}: {response}")

        finally:
            client_socket.close()

    def run_client(self):
        with open(self.url_file, "r") as file:
            urls = file.readlines()

        urls = [url.strip() for url in urls]
        threads = []

        for url in urls:
            thread = threading.Thread(target=self.send_request, args=(url,))

            threads.append(thread)

            thread.start()

            if len(threads) >= self.num_threads:
                for thread in threads:
                    thread.join()

                threads = []

        for thread in threads:
            thread.join()
