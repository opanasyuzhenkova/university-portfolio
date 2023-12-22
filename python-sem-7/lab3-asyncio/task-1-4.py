import asyncio
import aiohttp
import asyncpg
import json

# Делаем запросы к публичному API JSONPlaceholder и к базе данных PostgreSQL, предоставляемой ElephantSQL.

API_URL = "https://jsonplaceholder.typicode.com/posts"
DB_URL = "postgres://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs"


async def retrieve_api_data():
    async with aiohttp.ClientSession() as web_session:
        async with web_session.get(API_URL) as api_response:
            raw_data = await api_response.text()
            parsed_data = json.loads(raw_data)
            return parsed_data


async def retrieve_database_data():
    database_connection = await asyncpg.connect(DB_URL)
    database_query = "SELECT * FROM rnc_database LIMIT 10"
    query_results = await database_connection.fetch(database_query)
    await database_connection.close()
    return query_results


async def execute_async_tasks():
    api_data = await retrieve_api_data()
    db_data = await retrieve_database_data()

    print("API Data:")
    print(json.dumps(api_data, indent=4))
    print("\nDatabase Data:")
    for record in db_data:
        print(record)


if __name__ == "__main__":
    asyncio.run(execute_async_tasks())
