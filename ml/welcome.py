import pandas as pd
df=pd.read_csv("student_performance.csv")
print(df[["StudentName","Course"]])

