class Hat:
    
    def __init__(self, kind, color, material):
        self.kind = kind
        self.color = color
        self.material = material

myObject = Hat("", "", "")

print(myObject.kind + " " + myObject.color + " " + myObject.material)