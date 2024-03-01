# object_size = 10
# proximity = 100

# if object_size > 5 and proximity < 1000:
#     print("Evasive maneuvers required")
# else:
#     print("NOT A THREAT")

# --------------------------------------------------------
# --------------------------------------------------------
                # EXERCISE

# text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
# On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# # sentences = text.split(". ")
# # print(sentences)

# # for sentence in sentences:
# #     if 'temperature' in sentence:
# #         print(sentence)

# --------------------------------------------------------------



# -----------------------------------------------------------------
        #EXERCISE

# name = 'Ganymade'
# planet = 'Mars'
# gravity = 1.43

# template = """f(
# Gravity Facts about {name}
# -----------------------------------
# Planet Name : {planet}
# Gravity on {name}: {gravity} m/s2)
# """
# print(template.format(name=name, planet=planet, gravity=gravity))

# -----------------------------------------------------------------
#

# WORKING WITH NUMBERS AND CONVERTING

# from math import ceil, floor

# first_planet_input = input("Enter the distance from the sun for the first planet in km\n")
# second_planet_input = input("Enter the distance from the sun for the second planet in km\n")

# # converting from string to int

# first_planet = float(first_planet_input)
# second_planet = float(second_planet_input)

# # calculation

# distance_km = (second_planet - first_planet)
# print('Distance = ' + str(ceil(distance_km)))
# print('Distance_float = ' + str(distance_km))

# -----------------------------------------------------------------

# WORKING WITH PYTHON LISTS


# planets = ['Mercury', 'Earth', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune', 'Jupiter']

# print('First planet on the list is: ' + planets[0])
# print('Second planet on the list is: ' + planets[1])
# print('Third planet on the list is: ' + planets[2])

# planets[1] = 'Tierra'
# print(planets)

# # Lenght of a list
# number_of_planets = len(planets)
# print('Number of planets: ' + str(number_of_planets))

# # Append to list .append(value)

# planets.append('New Planet')
# new_number_of_planets = len(planets)
# print("New number of planets: ", new_number_of_planets)

# # finding a value in a list (jupiter)
# planets_loweredCase = [x.lower() for x in planets]
# jupiter_find_index = planets_loweredCase.index('jupiter')
# print('Jupiter is the ', jupiter_find_index + 1, 'planet from the sun')

# --------------------------------------------------------------

# More numbers exercise
# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# bus_weight = 124054

# print('On Earth, a double-checker bus weighs', bus_weight, 'N')
# print('On Mars, a double-decker bus weighs ', bus_weight*gravity_on_planets[1], 'N')
# print('The lightest a bus would be in solar system is ', bus_weight * min(gravity_on_planets), 'N')
# print('The heaviest a bus would be in solar system is ', bus_weight * max(gravity_on_planets), 'N')

# --------------------------------------------------------------

# Slice Lists
# planets = ['Mercury', 'Earth', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune', 'Jupiter']
# planets_before_earth = planets[0:1]
# print(planets_before_earth)

# planets_after_earth = planets[2:]
# # OR ---> planets_after_earth = planets[2::]
# print(planets_after_earth)

# --------------------------------------
# Joining and sorting lists
# planets = ['Mercury', 'Earth', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune', 'Jupiter']
# amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
# new_list_joined = planets + amalthea_group
# print(new_list_joined)

# # Sort list
# list_to_sort = planets + amalthea_group
# print('List not sorted: ', list_to_sort)
# list_to_sort.sort()
# print('\nSorted list: ', list_to_sort, '\n')

# EXERCISE
# planets_list = ['Mercury', 'Earth', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune', 'Jupiter']
# # making every word in lowercase
# planets = [x.lower() for x in planets_list]
# user_planet_input = input('Please enter the name of the planet\n\t')
# user_planet_input.lower()

# # searching the position of the planet introduced by the user

# planets_index = planets.index(user_planet_input)
# print('The planet is in position ', planets_index)

#/ --------------------------------------------------------------\
    # WHILE AND FOR LOOPS
# WHILE

# person_name = ''

# while person_name=='':
#     print('Please, complete the information below')
#     first_name = input('First Name: \n')
#     last_name = input('Last Name: \n')
#     person_name = first_name + last_name

# # # # # # # # # # # # # # # # # # # # # 

# Creating list with user inputs

# names = ''
# name_list = [] 

# while names.lower() != 'done':
#     if names:
#         name_list.append(names)
#     names = input("Please provide the list of names or 'done' when done\n")
#     print(name_list)


#     # FOR

# countdown = [4,3,2,1,0]
# for number in countdown:
#     print(number)
# print("Blast off!! 🚀")

# # Waiting a second for every iteration
# from time import sleep
# countdown = [4,3,2,1,0]
# for number in countdown:
#     print(number)
#     sleep(1)
# print("Blast off!! 🚀")

####   EXERCISE   ####
# from time import sleep
# from traceback import print_list

# names = ''
# names_list = []

# while names.lower() != 'done':
#     if names:
#         names_list.append(names)
#     names = input("Please provide a list of names, and 'done' when done\n")
#     #print(names_list)
    
# for names in names_list:
#         print(*names) #PRINTS IN SPACES EACH CHARACTER.
#         sleep(1)

  
    