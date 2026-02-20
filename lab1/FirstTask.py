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
    result_python = calculate_phyton(price_list, freights_list)
    endA = time.time()
    python_time = endA - startA

    startB = time.time()
    result_numpy = calculate_numpy(prices, freights)
    endB = time.time()
    numpy_time = endB - startB

    print(f"python время: {python_time:.6f} сек")
    print(f"numpy время: {numpy_time:.6f} сек")
    print(f"ускорение: {python_time / numpy_time:.2f}x")

    print(f"результаты совпадают: {np.allclose(result_python, result_numpy)}")

compare_speed()