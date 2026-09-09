# Задача 3
# базовый уровень
# Перепиши предыдущую задачу так, чтобы обе функции выполнялись параллельно через asyncio.gather(). Замерь новое время и сравни с предыдущим результатом.
import asyncio, time


async def task(name, delay):
    print(f"Задание {name} началось")
    await asyncio.sleep(delay)
    print(f'Задание {name} закончилось')

async def main():
    start = time.time()
    await asyncio.gather(
        task("Задание 1", 1),
        task("Задание 2", 2)
    )
    end = time.time()
    print(f"Время выполнения {end - start}")

asyncio.run(main())
