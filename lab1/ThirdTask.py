import numpy as np
import pandas as pd

df_products = pd.read_csv('olist_products_dataset.csv')

length = df_products['product_length_cm'].values
height = df_products['product_height_cm'].values
width = df_products['product_width_cm'].values

volumetric_weight = (length * height * width) / 6000
df_products['volumetric_weight'] = volumetric_weight

clean_weight = volumetric_weight[~np.isnan(volumetric_weight)]

print('объемный вес посчитан для', len(volumetric_weight), 'товаров')
print('из них', len(volumetric_weight) - len(clean_weight), 'товаров с пропущенными размерами')
print('первые пять значений:', volumetric_weight[:5])
print('средний объемный вес (без учета пропусков):', np.mean(clean_weight).round(3))


np.random.seed(42)
prices = np.random.randint(50, 500, size=(1000, 5))
coeffs = np.array([1.0, 1.15, 0.85, 1.2, 0.95])#взял из головы

final_prices = prices * coeffs

print('было:', prices[0])
print('коэффициенты:', coeffs)
print('стало:', final_prices[0].round(2))
print('размерность осталась:', final_prices.shape)


