file = open("example.txt", "a")
file.write("I love programming!")
file.close()

file = open("example.txt", "r")
print(file.read())