# WORKING WITH NUMBERS AND CONVERTING

from math import ceil, floor

first_planet_input = input("Enter the distance from the sun for the first planet in km\n")
second_planet_input = input("Enter the distance from the sun for the second planet in km\n")

# # converting from string to int

first_planet = float(first_planet_input)
second_planet = float(second_planet_input)

# # calculation

distance_km = (second_planet - first_planet)
print('Distance = ' + str(ceil(distance_km)))
print('Distance_float = ' + str(distance_km))