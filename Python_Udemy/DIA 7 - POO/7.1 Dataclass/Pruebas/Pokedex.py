class Pokemon:
	def __init__(self, Entry, Name, Type, Description, Is_caugth):
		self.Entry = Entry
		self.Name = Name
		self.Type = Type
		self.Description = Description
		self.Is_caught = Is_caugth

	def speak(self):
		print(self.Name)

	def display_details(self):
		print(f"Entry Number: {self.Entry}\n"
			  f'Name: {self.Name}\n'
			  f'Type: {self.Type}\n'
			  f'Description: {self.Description}')
		if self.Is_caught:
			print(f"{self.Name} is already caught!")
		else:
			print(f"{self.Name} is not caught yet!")


Pokemon1 = Pokemon(25, "Pikachu", "Electric",
				   "When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.",
				   Is_caugth=True)
Pokemon2 = Pokemon(6, "Charizard", "Flame",
				   "If Charizard becomes truly angered, the flame at the tip of its tail burns in a light blue shade.",
				   Is_caugth=False)
Pokemon3 = Pokemon(2, "Ivysaur", "Grass",
				   "The more sunlight Ivysaur bathes in, the more strength wells up within it, allowing the bud on its back to grow larger.",
				   Is_caugth=True)

Pokemon1.display_details()
print("\n")
Pokemon2.display_details()
print("\n")
Pokemon3.display_details()
