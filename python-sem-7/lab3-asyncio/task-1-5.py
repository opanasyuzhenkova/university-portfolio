import aiohttp
import asyncio


class WebScraper:
    def __init__(self, source_file):
        self.source_file = source_file

    async def retrieve_content(self, web_session, page_url):
        async with web_session.get(page_url) as response:
            return await response.text()

    async def harvest_page_data(self, page_url):
        async with aiohttp.ClientSession() as web_session:
            page_content = await self.retrieve_content(web_session, page_url)
            print(page_content)

    async def execute_harvesting(self):
        harvest_tasks = []
        with open(self.source_file, 'r') as file:
            page_urls = file.read().splitlines()

        for page_url in page_urls:
            task = asyncio.create_task(self.harvest_page_data(page_url))
            harvest_tasks.append(task)

        await asyncio.gather(*harvest_tasks)


if __name__ == "__main__":
    url_list_file = "page_urls.txt"
    data_harvester = WebScraper(url_list_file)

    asyncio.run(data_harvester.execute_harvesting())
