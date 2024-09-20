class vacation:

    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather

    def tuesday(self):
        print("We will be hiking on Tuesday.")
summer = vacation("Hawaii", 2000, "Sunny")
print(vacation.weather)
summer.rating = 10

print(summer)

summer.weather = "rainy"
print(summer.rating)
print(summer.weather)