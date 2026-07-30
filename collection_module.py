import collections

Student = collections.namedtuple("Student", ["name", "age", "rollno"])
s1=Student("John", 20, 101)
s2=Student("Alice", 22, 102)
print(s1.name, s1.age, s1.rollno)