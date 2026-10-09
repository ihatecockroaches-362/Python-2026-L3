import pandas as pd

df = pd.read_csv('students.csv')
ds = pd.read_csv("scores.csv")
print("first 5 rows")
print(df.head())

rows, cols = df.shape
print(f"\nRows: {rows}, Columns: {cols}")

name_and_gpa = df[["name", "GPA"]]
print("\nName and GPA")
print(name_and_gpa.head())

high_gpa_students = df[df['GPA'] >= 3.5]
print("\nStudents with GPA >=3.5")
print(high_gpa_students)

sorted_students = df.sort_values(by='GPA', ascending=False)
print("\nGPA Descending: ")
print(sorted_students)

avg_gpa_by_major = df.groupby('major')['GPA'].mean().reset_index()
print("\nGPA by major")
print(avg_gpa_by_major)
df = df.fillna(0)
ds = ds.fillna(0)

print("\nFill no available cells with 0")
print(df)
print(ds)

print("\nNew table after merging")
da = pd.merge(df,ds, on = "student_id")
score_col = ['python','math','database']
da["average"] = da[score_col].mean(axis=1)
da = da.fillna(0)
print(da)

print("\nTop 5 students with the highest average")
top5_avg = da.sort_values(by = "average", ascending = False).head(5).reset_index()
print(top5_avg)

print("\nAverage by major")
avg_by_major = da.groupby("major")["average"].mean().reset_index()
print(avg_by_major)