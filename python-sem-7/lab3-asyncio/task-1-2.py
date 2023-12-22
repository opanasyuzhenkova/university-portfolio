import asyncio
import time
from termcolor import colored
from pynput import keyboard


# Улучшаем предыдущую программу, распечатываем текущие дату и время в одной строке разными цветами.
# Добавляем обработку нажатия клавиши Esc для выхода из программы.

async def print_current_time_colored():
    try:
        while True:
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            colorful_time = colored(formatted_time, "green")
            print(f"\rТекущее время: {colorful_time}", end="")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass


async def run_time_display():
    display_task = asyncio.create_task(print_current_time_colored())

    try:
        await display_task
    except KeyboardInterrupt:
        pass
    finally:
        display_task.cancel()


def on_escape_key(key):
    if key == keyboard.Key.esc:
        print("\nExiting program.")
        time_loop.stop()


if __name__ == "__main__":
    time_loop = asyncio.get_event_loop()

    try:
        time_loop.run_until_complete(run_time_display())
        with keyboard.Listener(on_release=on_escape_key) as key_listener:
            time_loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        time_loop.close()
