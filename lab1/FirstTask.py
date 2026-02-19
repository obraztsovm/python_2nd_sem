import pandas as pd
import numpy as np
import time


df = pd.read_csv('olist_order_items_dataset.csv')
prices = df['price'].values
freights = df['freight_value'].values
price_list = df['price'].tolist()
freights_list = df['freight_value'].tolist()

def calculate_phyton(price_list, freight_list):
    total_list = []

    for price, freight in zip(price_list, freight_list):
        if price > 500:
            discount = 0.15
        elif price > 100:
            discount = 0.10
        else:
            discount = 0.0

        total = ( price * (1 - discount) ) + freight
        total_list.append(total)

    return total_list

def calculate_numpy(prices, freights):
    conditions = [
        prices > 500,
        prices > 100,
        prices < 100
    ]

    discounts = [0.15, 0.10, 0.0]
    discount_mask = np.select(conditions, discounts)

    return (prices * (1 - discount_mask)) + freights

def compare_speed():
    startA = time.time()
    python_time = time.time() - startA

    startB = time.time()
    numpy_time = time.time() - startB

    print(f"Python время: {python_time:.10f} сек")
    print(f"NumPy время: {numpy_time:.10f} сек")
    print(f"Ускорение: {python_time / numpy_time:.5f}x")

compare_speed()