class Pokemon:
    def __init__(self):
        self.entry = int(input("Pokemon Entry: "))
        self.name = str(input("Pokemon Name: "))
        types_input = input("Pokemon Types (comma-separated): ")
        self.types = types_input.split(",")
        self.description = str(input("Pokemon Description: "))
        caught_input = input("Caught? (True/False): ").lower()
        self.is_caught = caught_input == "false"
  
    def speak(self):
        print(f"{self.name} {self.name}")
  
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught!")

poke1 = Pokemon()
poke2 = Pokemon()
poke3 = Pokemon()

poke1.display_details()
poke2.speak()
poke3.display_details()
