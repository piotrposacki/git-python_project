import os

os.chdir("C:\\logs")
print(os.getcwd())

print(os.listdir())
for file in os.listdir():
    with open(file) as current:
        print(current.readline())
