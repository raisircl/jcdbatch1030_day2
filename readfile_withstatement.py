with open("student_notes.txt", "r") as file:
    data = file.read()

print(data)

# No need to write file.close() manually
