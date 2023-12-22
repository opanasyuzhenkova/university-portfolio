import threading
import time


def set_event(e):
    while True:
        time.sleep(1)
        e.set()


def wait_event(e):
    print("Waiting for event...")
    e.wait()
    print("Event occurred")


def check_event(e):
    while not e.is_set():
        print("No event")
        time.sleep(1)


if __name__ == "__main__":
    evt = threading.Event()
    setter = threading.Thread(target=set_event, args=(evt,))
    waiter = threading.Thread(target=wait_event, args=(evt,))
    checker = threading.Thread(target=check_event, args=(evt,))

    setter.start()
    waiter.start()
    checker.start()

    waiter.join()
    checker.join()

    print("Threads finished.")
