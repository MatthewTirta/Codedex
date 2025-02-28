# Write code below 💖

class City:
  def __init__(self, name, country, population, landmarks, restaurants):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.restaurants = restaurants

japan = City("Tokyo", "Japan", "100000", "Tokyo Tower", "Musoshin Ramen")

jakarta = City("Jakarta", "Indonesia", "280000000", ["Monas", "Galeri Nasional", "Pancoran"], "Bakmi Asui")

print(vars(japan))
print(vars(jakarta))