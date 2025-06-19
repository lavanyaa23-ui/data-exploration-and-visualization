import pandas as pd
# Sample employee dataset
data2 = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Hours_Worked': [160, 150, 170, 165, 155, 145]
}

df2 = pd.DataFrame(data2)

# Group by department and compute total hours
grouped_hours = df2.groupby('Department')['Hours_Worked'].agg(['sum', 'mean']).reset_index()

print("\nTotal and Average Hours Worked by Department:")
print(grouped_hours)

# Create a pivot table (if required in presentation format)
pivot_summary = pd.pivot_table(df2, values='Hours_Worked', index='Department', aggfunc=['sum', 'mean'])

print("\nPivot Summary Report:")
print(pivot_summary)

# Identify department with highest average hours
max_avg_dept = grouped_hours.loc[grouped_hours['mean'].idxmax(), 'Department']
print(f"\nDepartment with highest average working hours: {max_avg_dept}")
