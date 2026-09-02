import pandas as pd

df = pd.read_csv("dirty_data.csv")

df = df.drop_duplicates()
df["StudentName"] = df["StudentName"].str.strip()
df["Gender"] = df["Gender"].str.strip().str.title()

df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")
df["FinalMarks"] = pd.to_numeric(df["FinalMarks"], errors="coerce")

df.loc[(df["Attendance"] < 0) | (df["Attendance"] > 100), "Attendance"] = pd.NA
df.loc[(df["FinalMarks"] < 0) | (df["FinalMarks"] > 100), "FinalMarks"] = pd.NA

# Fill remaining missing values
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())
df["FinalMarks"] = df["FinalMarks"].fillna(df["FinalMarks"].median())

# Save cleaned file
df.to_csv("cleaned_student_performance.csv", index=False)

print("Cleaned dataset saved successfully")
