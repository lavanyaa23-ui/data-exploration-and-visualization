import pandas as pd

# Sample data
data = [
    {"employee": "Alice", "department": "HR", "hours": 40},
    {"employee": "Bob", "department": "IT", "hours": 45},
    {"employee": "Charlie", "department": "HR", "hours": 38},
    {"employee": "David", "department": "Finance", "hours": 42},
    {"employee": "Eva", "department": "IT", "hours": 50},
    {"employee": "Frank", "department": "Finance", "hours": 39}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Create pivot table: Sum of hours grouped by department
pivot = pd.pivot_table(df, values='hours', index='department', aggfunc='sum')

print("Work Hours by Department (Pivot Table):")
print(pivot)
