import pandas as pd

df = pd.read_csv("dirty_data.csv")
# Count missing values in each column
print(df.isnull().sum())

# Check total missing values
print("Total missing values:")
print(df.isnull().sum().sum())
# Show rows where any value is missing
missing_rows = df[df.isnull().any(axis=1)]

print(missing_rows)

# Fill missing Attendance with average Attendance
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

# Fill missing FinalMarks with average FinalMarks
df["FinalMarks"] = df["FinalMarks"].fillna(
    df["FinalMarks"].mean()
)

# Fill missing Gender with Unknown
df["Gender"] = df["Gender"].fillna("Unknown")

# Fill missing Result with Not Available
df["Result"] = df["Result"].fillna("Not Available")

# Remove rows that contain any missing value
clean_df = df.dropna()

print(clean_df)

# Remove rows only if FinalMarks is missing
clean_df = df.dropna(subset=["FinalMarks"])

# Count duplicate rows
print(df.duplicated().sum())

# Show duplicate rows
duplicates = df[df.duplicated()]

print(duplicates)


# Remove duplicate rows
df = df.drop_duplicates()

print(df)

# Check again
print("Duplicates after cleaning:")
print(df.duplicated().sum())

# Check data types
print(df.dtypes)

# Convert columns to numeric
df["Attendance"] = pd.to_numeric(
    df["Attendance"],
    errors="coerce"
)

df["FinalMarks"] = pd.to_numeric(
    df["FinalMarks"],
    errors="coerce"
)


# Remove extra spaces from names
df["StudentName"] = df["StudentName"].str.strip()

# Remove spaces from Gender also
df["Gender"] = df["Gender"].str.strip()

print(df[["StudentName", "Gender"]])


# Convert gender values into same format
df["Gender"] = df["Gender"].str.title()

print(df["Gender"].value_counts())

# male, MALE, Male become Male
# female, FEMALE, Female become Female
# Attendance should be between 0 and 100
invalid_attendance = df[
    (df["Attendance"] < 0) |
    (df["Attendance"] > 100)
]

print(invalid_attendance)

# Marks should be between 0 and 100
invalid_marks = df[
    (df["FinalMarks"] < 0) |
    (df["FinalMarks"] > 100)
]


# Replace invalid Attendance with NaN
df.loc[
    (df["Attendance"] < 0) | (df["Attendance"] > 100),
    "Attendance"
] = pd.NA

# Replace invalid FinalMarks with NaN
df.loc[
    (df["FinalMarks"] < 0) | (df["FinalMarks"] > 100),
    "FinalMarks"
] = pd.NA
# Median is often safer when data has extreme values
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].median()
)

df["FinalMarks"] = df["FinalMarks"].fillna(
    df["FinalMarks"].median()
)

# Rename columns for better readability
df = df.rename(columns={
    "StudentName": "Name",
    "FinalMarks": "Marks",
    "StudyHours": "DailyStudyHours"
})

print(df.columns)
