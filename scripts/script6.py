import pandas as pd

# Приклад датафрейму
df = pd.DataFrame({
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'Sales': [1500.45, 2300.10, 1800.55, 2200.99, 1950.75, 2500.33],
    'Commission': [30000, 60000, 45000, 70000, 52000, 48000]
})

df['Sales'] = df['Sales'].round(1)


def easefun(el):
    if(el>50000):
        return "High Deal"
    else:
        return "Regular Deal"

df['DealType'] = df['Commission'].apply(easefun)


df1 = df[df['DealType'] == "High Deal"]

df_group = df.groupby('Month').agg({
    'Sales': 'sum',
    'Commission': 'mean'
})

df_group = df_group.sort_values(by='Sales',ascending=False)

print(df_group)