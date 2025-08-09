import pandas as pd

df = pd.read_csv('data/data1.csv') # читаємо датафрейм з файлу

print(df.info()) # витягуємо інформацію про датафрейм


manual_df = pd.DataFrame([
    {"name_car":'TOYOTA', "price":100000, "color":'red'},
    {"name_car":'BMW', "price":200000, "color":'blue'},
    {"name_car":'AUDI', "price":300000, "color":'green'},
    {"name_car":'MERCEDES', "price":400000, "color":'yellow'},
    {"name_car":'VOLVO', "price":500000, "color":'black'},
    {"name_car":'VOLKSWAGEN', "price":600000, "color":'white'},
    {"name_car":'MAZDA', "price":700000, "color":'gray'},
    {"name_car":'NISSAN', "price":800000, "color":'brown'},
    {"name_car":'HYUNDAI', "price":900000, "color":'pink'}
])

mn_df_copy = manual_df.copy(deep=True) # створюємо копію датафрейму


# print(df.head()) # витягуємо перші '5' елементів

# print(df.tail()) # витягуємо останні '5' елементів

# print(mn_df_copy['name_car']) # витягуємо колонку 'name_car'

# print(df[0]) # витягуємо перший елемент

# print(df[0:3]) # витягуємо перші '3' елементів

# df.to_csv('saved/data1.csv', index=False) # зберігаємо датафрейм у файл

# print(df.shape) # витягуємо розмір датафрейму отримуємо 9 рядків і 3 стовпців

# print(df.columns.tolist()) # витягуємо назви колонок і перетворюємо їх у список

# print(df.dtypes) # витягуємо типи даних для колонок

# print(df.values) # витягуємо двовимірний масив даних

# print(df.values[2,1]) # витягуємо значення з 2-го рядка і 1-го стовпця

# print(df.describe()) # оброблює тільки числові дані та показує статистичні дані 

# print(df.isna()) # показує чи є в датафреймі пропущені значення

