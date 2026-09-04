import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("Libraries imported successfully")

df = pd.read_csv("cleaned_student_performance.csv")

# print(df.head())
# print(df.info())
# print(df.describe())
features = [
    "Attendance",
    "StudyHours",
    "PreviousMarks"
]

X = df[features]
y = df["FinalMarks"]

print(X.head())
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

model = LinearRegression()

model.fit(X_train, y_train)

print("Model training completed")

y_pred = model.predict(X_test)

print("Actual Marks:")
print(y_test.values)

print("Predicted Marks:")
print(y_pred)

result_df = pd.DataFrame({
    "ActualMarks": y_test.values,
    "PredictedMarks": y_pred
})

print(result_df)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)


new_student = pd.DataFrame({
    "Attendance": [80],
    "StudyHours": [4],
    "PreviousMarks": [70]
})

predicted_marks = model.predict(new_student)

print("Predicted Final Marks:", predicted_marks[0])
