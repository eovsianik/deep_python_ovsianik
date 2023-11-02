import socket
import threading
import requests
from bs4 import BeautifulSoup
from collections import Counter
import json
from queue import Queue


class WorkerMaster:
    def __init__(self, listen_address, num_workers):
        self.listen_address = listen_address
        self.num_workers = num_workers
        self.workers = []
        self.total_urls_processed = 0
        self.queue = Queue()

    def crawl_url(self, url, k):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            words = text.split()
            word_counts = Counter(words)

            top_words = word_counts.most_common(k)

            result = {word: count for word, count in top_words}
            result_json = json.dumps(result)

            return result_json

        else:
            return None

    def handle_request(self, client_socket, client_address):
        url = client_socket.recv(1024).decode()

        result = self.crawl_url(url, 5)

        client_socket.send(result.encode())

        client_socket.close()
        self.total_urls_processed += 1

        print(f"Обработано URL-адресов: {self.total_urls_processed}")

    def start(self):
        for _ in range(self.num_workers):
            worker_thread = threading.Thread(target=self.worker_loop)
            worker_thread.start()
            self.workers.append(worker_thread)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(self.listen_address)
        server_socket.listen()

        while True:
            client_socket, client_address = server_socket.accept()

            self.queue.put((client_socket, client_address))

    def stop(self):
        for worker_thread in self.workers:
            worker_thread.join()

    def worker_loop(self):
        while True:
            client_socket, client_address = self.queue.get()

            self.handle_request(client_socket, client_address)
