import numpy as np
import pandas as pd

df_products = pd.read_csv('olist_products_dataset.csv')

df_sample = df_products[['product_weight_g', 'product_length_cm',
                         'product_height_cm', 'product_width_cm']].iloc[:1000].copy()
df_sample = df_sample.dropna()
features = df_sample.values.astype(float)

min_vals = features.min(axis=0)
max_vals = features.max(axis=0)
features_norm = (features - min_vals) / (max_vals - min_vals + 1e-10)

target_idx = 40
target_vector = features_norm[target_idx].reshape(1, -1)

dot_product = np.dot(features_norm, target_vector.T).flatten()
norm_features = np.linalg.norm(features_norm, axis=1)
norm_target = np.linalg.norm(target_vector)

cosine_similarities = dot_product / (norm_features * norm_target + 1e-10)
df_sample['similarity'] = cosine_similarities

print('размер матрицы признаков:', features.shape)
print('целевой товар (индекс', target_idx, '), его нормализованные признаки:', target_vector[0].round(2))
print()
print('5 самых похожих товаров:')
print(df_sample.sort_values('similarity', ascending=False).iloc[1:6][['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm', 'similarity']].round(3))
print()
print('5 самых непохожих товаров:')
print(df_sample.sort_values('similarity').iloc[:5][['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm', 'similarity']].round(3))


