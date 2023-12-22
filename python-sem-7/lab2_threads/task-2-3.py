import concurrent.futures
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import BoundedSemaphore

# List of new image URLs
image_sources = [
    "https://unsplash.com/photos/a-couple-of-people-walking-across-a-sandy-beach-Dsi8GmJTBcU",
    "https://unsplash.com/photos/a-lantern-in-the-middle-of-a-snowy-field-3SoNm_Xvys8",
]

download_directory = 'downloaded_images'
os.makedirs(download_directory, exist_ok=True)
download_semaphore = BoundedSemaphore(value=2)


def save_image(url, file_path):
    response = requests.get(url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)


def async_image_download(url, file_path):
    with download_semaphore:
        save_image(url, file_path)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=len(image_sources)) as executor:
        download_tasks = {executor.submit(async_image_download, url, os.path.join(download_directory, f"image_{index}.jpg")): url for index, url in enumerate(image_sources)}

        for task in as_completed(download_tasks):
            source_url = download_tasks[task]
            try:
                task.result()
                print(f"Downloaded: {source_url}")
            except Exception as error:
                print(f"Failed to download {source_url}. Error: {error}")
