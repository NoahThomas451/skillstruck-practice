file = open("porupine.txt", "w")
file.write("In short, I love to code!")
file.close()

file = open("porcupine.txt", "r")
print(file.read())
