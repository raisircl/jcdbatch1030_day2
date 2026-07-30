import os
print("Current Working Directory:", os.getcwd())
#os.mkdir("songs")
#os.chdir("songs")
#print("NOW Current Working Directory:", os.getcwd())
#os.chdir("..")
#print("after .. Current Working Directory:", os.getcwd())
#os.rmdir("songs")

#print(os.listdir())

for i in os.listdir():
    print(i)