from math import pi; from random import choice as ch

planets = [
	'Mercury',
	'Venus',
	'Earth',
	'Mars',
	'Saturn'
]

random_planet = ch(planets)
r = 0
if random_planet == "Mercury":
	r = 2240
elif random_planet == "Venus":
	r = 6052
elif random_planet == "Earth":
	r = 6371
elif random_planet == "Mars":
	radio = 3390
elif random_planet == "Saturn ":
	r = 58232
else:
	print("Oops! An error ocurred.")

area = round(4 * pi * r ** 2)

print(f"Planet {random_planet} area is {area}")