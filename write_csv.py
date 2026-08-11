with open("students.csv", "w") as file:
    file.write("StudentID,Name,Attendance,Marks\n")
    file.write("1,Rahul,85,78\n")
    file.write("2,Priya,92,88\n")
    file.write("3,Aman,60,49\n")

print("CSV file created")
