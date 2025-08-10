from operator import index
from numpy import inner
import pandas as pd


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


manual_df['engine'] = 2000 #додавання нового стовпця до даних

manual_df['engine'] = [200,300,400,700,400,300,400,230,120] #додавання до кожного елемента

manual_df.loc[manual_df['engine'] == 200,'engine'] = 400 # За допомогою лок змінюємо оскільки якщо просто попробувати через фільтер то будемо отримувати комі. і нічого не змінимо

print(manual_df)


manual_df2 = pd.DataFrame([
    {"count_of_while":20},
    {"count_of_while":30},
    {"count_of_while":50},
    {"count_of_while":10},
    {"count_of_while":50},
    {"count_of_while":20},
    {"count_of_while":40},
    {"count_of_while":90},
    {"count_of_while":10}
   ])


df = pd.concat([manual_df,manual_df2],axis=1)

df = manual_df.merge(manual_df2, how='inner', left_index=True, right_index=True)

df.drop('count_of_while',axis = 1,inplace=True)

print(df)