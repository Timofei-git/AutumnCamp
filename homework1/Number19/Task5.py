# Задача 5
# средний уровень
# Есть список из 5 строк-«адресов». Напиши функцию fetch(url), которая через await asyncio.sleep(1) имитирует запрос и возвращает f"Ответ от {url}".
# Обработай все 5 адресов параллельно через gather, выведи каждый результат и общее время выполнения — оно должно получиться около 1 секунды, а не 5.
import asyncio
import time


async def fetch(url):
    print(f'Запрос к {url}')
    await asyncio.sleep(1)
    return f'Получен ответ от {url}'

async def main():
    urls = [
        "https://example.com",
        "https://openai.com",
        "https://anthropic.com",
        "https://github.com",
        "https://python.org"
    ]

    start = time.time()
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    end = time.time()
    print(f'Время выполнения {end - start}')
    for result in results:
        print(result)

asyncio.run(main())