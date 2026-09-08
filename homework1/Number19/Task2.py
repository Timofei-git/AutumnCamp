# Задача 2
# базовый уровень
# Напиши две асинхронные функции с разным временем ожидания (1 и 2 секунды). Запусти их последовательно через await, замерь и выведи общее время выполнения.
import asyncio


async def task(name, delay):
    print(f"Задание {name} началось")
    await asyncio.sleep(delay)
    print(f'Задание {name} закончилось')

asyncio.run(task("Задание 1", 1))
asyncio.run(task("Задание 2", 2))