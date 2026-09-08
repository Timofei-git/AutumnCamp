# Задача 1
# базовый уровень
# Напиши асинхронную функцию, которая ждёт 1 секунду через await asyncio.sleep(1), а затем печатает «Готово». Запусти её через asyncio.run().
import asyncio

async def task():
    print("Задание началось")
    await asyncio.sleep(1)
    print('Задание готово')

asyncio.run(task())