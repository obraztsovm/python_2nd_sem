import numpy as np
import pandas as pd

df_items = pd.read_csv('olist_order_items_dataset.csv')
prices = df_items['price'].values

#Булево индексирование
average_price = np.mean(prices)
std_price = np.std(prices)
three_sigma = 3 * std_price
upper_bound = average_price + three_sigma

anomaly_mask = prices > upper_bound
anomalies = df_items[anomaly_mask]

print(f"Средняя цена: {average_price:.2f} BRL")
print(f"Порог (average + 3σ): {upper_bound:.2f} BRL")
print(f"Найдено аномалий: {len(anomalies)}")
print("Примеры аномалий:")
print(anomalies[['order_id', 'product_id', 'price']].head())

#Fancy Indexing
total_rows = len(prices)
random_indices = np.random.choice(total_rows, size=100, replace=False)
random_orders = df_items.iloc[random_indices]

print(f"\nВыбрано случайных заказов: {len(random_orders)}")
print("Первые 5 случайных заказов:")
print(random_orders[['order_id', 'product_id', 'price']].head())