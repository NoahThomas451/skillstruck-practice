class Person:
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("Jasmine", "15", "Female")
p2 = Person("George", "67", "Male")

print(p1.name + " " + p1.age + " " + p1.gender)
print(p2.name + " " + p2.age + " " + p2.gender)