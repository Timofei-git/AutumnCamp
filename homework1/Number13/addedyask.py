# С помощью zip и dict собери словарь shop_month_sales, где ключ — название магазина, а значение — словарь вида {месяц: продажи} (как ты уже делал с оценками студентов).
# Напиши код, который для каждого магазина выводит суммарные продажи за все месяцы, игнорируя значения None (считай их как 0 или просто пропускай).
# Выведи название магазина(-ов), у которых средние продажи за месяц выше 1300 (среднее считать только по месяцам, где есть реальные данные, т.е. None не учитывать ни в сумме, ни в количестве месяцев).
# (усложнение, если хочешь дожать до уровня выше среднего): сделай отдельный словарь best_month_per_shop, где для каждого магазина указан месяц с максимальными продажами.


shop_names = ["Sunny Market", "Green Grocery", "City Fresh"]
months = ["January", "February", "March", "April"]
shop_sales = [
    [1200, 1500, 900, 1700],
    [800, None, 950, 1100],
    [2000, 2100, None, 2300]
]

shop_month_sales = {
    name: dict(zip(months, sales))
    for name, sales in dict(zip(shop_names, shop_sales)).items()
}

print(shop_month_sales)

for shops, month_sales in shop_month_sales.items():
    summary = 0
    count = 0
    for month, sales in month_sales.items():
        if sales is None:
            continue
        summary += sales
        count += 1
    print(f'The sum of the sales for {shops} is {summary}')
    if count != 0 and summary / count > 1300:
        print(f'Shop {shops} has a sale of {summary / count:.2f}.')

best_month_per_shop = {}
for shop, values in shop_month_sales.items():
    best_month = None
    best_value = -1
    for month, sales in values.items():
        if sales is None:
            continue
        if best_value < sales:
            best_month = month
            best_value = sales

    best_month_per_shop[shop] = [best_month, best_value]

print(best_month_per_shop)







