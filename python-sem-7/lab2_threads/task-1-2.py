import requests
import threading


urls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSb_N4umbFejqkrOVdFJX9rV6DZHsm9oyzJsQ9vXqgI6Q&s",
]


def download_image(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Загружен файл: {file_name}")
    else:
        print(f"Не удалось загрузить файл: {url}")


def main():
    threads = []

    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()