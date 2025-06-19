import pandas as pd
data = {
    'City': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Chennai'],
    'Date': pd.to_datetime([
        '2024-06-10', '2024-06-17', '2024-07-03', '2024-07-10',
        '2024-08-05', '2024-08-15', '2024-06-12', '2024-07-20'
    ]),
    'Temperature': [40, 42, 34, 33, 41, 35, 37, 36]
}

df = pd.DataFrame(data)
df['Month'] = df['Date'].dt.month
grouped = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()
pivot_table = grouped.pivot(index='City', columns='Month', values='Temperature').fillna(0)

print("Month-wise Temperature Summary:")
print(pivot_table)
summer_months = [6, 7, 8]
pivot_table['Summer_Total'] = pivot_table[summer_months].sum(axis=1)
hottest_city = pivot_table['Summer_Total'].idxmax()
print(f"\nCity with highest total summer temperature: {hottest_city}")
