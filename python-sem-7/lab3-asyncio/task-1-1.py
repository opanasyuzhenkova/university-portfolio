import asyncio
import time

# Создаем простую асинхронную функцию, которая в бесконечном цикле отображает текущее время с интервалом 1 секунда,
# и запускаем ее с помощью asyncio. Завершать программу можно через комбинацию клавиш типа Ctrl + C или Ctrl + Break.

async def display_current_time():
    try:
        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Current time: {current_time}")
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass

async def main_async():
    await display_current_time()

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main_async())
    except KeyboardInterrupt:
        pass
    finally:
        event_loop.close()
