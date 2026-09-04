import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_student_performance.csv")

print(df.head())

# Line chart: student marks
plt.figure(figsize=(8, 5))

plt.plot(
    df["StudentName"],
    df["FinalMarks"],
    marker="o",
    color="green"
)

plt.title("Student Final Marks")
plt.xlabel("Student")
plt.ylabel("Final Marks")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
