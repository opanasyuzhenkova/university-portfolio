import requests
import concurrent.futures


def fetch_content(url):
    response = requests.get(url)
    return response.text


def main():
    target_urls = [
        "https://www.python.org/doc/",
        "https://github.com",
        "https://realpython.com"
    ]

    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(fetch_content, url): url for url in target_urls}

        for completed_future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[completed_future]
            try:
                content = completed_future.result()
                print(f"Request to {url} completed successfully.")
                results.append(content)
            except Exception as e:
                print(f"Request to {url} failed with error: {str(e)}")

if __name__ == "__main__":
    main()
