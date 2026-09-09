# Задача 4
# средний уровень
# Напиши асинхронную функцию fetch_data(id), которая имитирует «запрос к серверу» через await asyncio.sleep(1) и возвращает строку с этим id.
# Запусти пять таких вызовов параллельно через gather и выведи все результаты.
import asyncio


async def fetch_data(id):
    print("Выполняем запрос к серверу")
    await asyncio.sleep(1)
    print("Запрос выполнен")
    return id

async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
        fetch_data(4),
        fetch_data(5)
    )

    print(results)

asyncio.run(main())

