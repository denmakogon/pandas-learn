import pandas as pd

df = pd.read_csv('data/Home_Sale_Data.csv')

df['SaleDate'] = pd.to_datetime(df['SaleDate'])

df['DayName'] = df['SaleDate'].dt.day_name() #додавання дня тижня до даних в залежності від дати

df['Commision'] = df['SalePrice'] * 0.1 # обчислюємо стовпець на остнові даних

df['Difference'] = df['AskingPrice'] - df['SalePrice'] #обчислюємо різницю між цінами




def deal_type_fun(el):
    if el>50000:
        return 'High Deal'
    else:
        return 'Regular Deal'

df['DealType'] = df['Commision'].apply(deal_type_fun)


print(df.info())