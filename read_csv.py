with open("students.csv", "r") as file:
    for line in file:
        row=line.strip().split(",")
        for col in row:
            #print(f"{col:<15}","\t", end="")
            print("%15s" % col, end="\t")
        print()
