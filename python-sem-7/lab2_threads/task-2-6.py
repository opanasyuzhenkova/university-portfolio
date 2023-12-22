import threading
import time


class CommunicationCoordinator:
    def __init__(self):
        self.sync_barrier = threading.Barrier(2)

    def server_interaction(self):
        print("Server is waiting...")
        self.sync_barrier.wait()
        print("Server received request")

    def client_interaction(self):
        print("Client is preparing...")
        time.sleep(2)
        print("Client is ready!")
        self.sync_barrier.wait()


if __name__ == "__main__":
    coordinator = CommunicationCoordinator()
    server_thread = threading.Thread(target=coordinator.server_interaction)
    client_thread = threading.Thread(target=coordinator.client_interaction)
    server_thread.start()
    client_thread.start()
    server_thread.join()
    client_thread.join()
