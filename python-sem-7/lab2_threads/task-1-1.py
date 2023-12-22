import threading

# Create multiple threads and output their names from within each thread.


def print_thread_name():
    thread_name = threading.current_thread().name
    print(f"Hello world! My name is {thread_name}!")


def main():
    num_threads = 10
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=print_thread_name)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
