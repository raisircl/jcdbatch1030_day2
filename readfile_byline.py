file = open("student_notes.txt", "r")

for line in file:
    print(line.strip())

file.close()
