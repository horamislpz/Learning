# Learning Python - Calculator

# while True:
#     operation = str(input("Type of operation: + = Sum, - = Minus and * = Factor\n"))
#     if operation == '+':
#         first_number = float(input("\nType the first number: \n"))
#         second_number = float(input("\nType the second number: \n"))
#         result = first_number + second_number
#         print("THE SUM OF THE TWO NUMBERS PROVIDED = " + str(result))
#         break 
#     else :{
#     print("YOU MUST INDICATE THE TYPE OF OPERATION\n")      
#     }

# --------------------------------------------------------

# object_size = 10
# proximity = 100

# if object_size > 5 and proximity < 1000:
#     print("Evasive maneuvers required")
# else:
#     print("NOT A THREAT")

# --------------------------------------------------------
# Using tripple quotations like a line breaker or text editor
# using ".tittle() to print initial in caps"

# multiline = """
# Facts about the Moon:
# There is no atmosphere
# There is no sound.
#             """
# print(multiline.title())
# --------------------------------------------------------

# SPLIT A STRING
# saving it in a list.

# temperatures = "this method helps separate the string at every space, like this. 9 38"
# temperatures_list = temperatures.split()
# print(temperatures_list)

# -------------------------------------------------------

# Finding and counting words in a string

# print("Word" in "We are only trying to see if Python can find the Word in this string, if returns False is because is not here")
# ---------
# words = ("""We are only trying to see if Python can find the Word in this string, if returns False is because is not here""".lower())
# print(words.find("word"))
# print(words.count("only"))
# print(words.count("i"))

# --------------------------------------------------------

# CHECKING CONTENT
# temperatures = "Mars Average Temperatures: -60 C And -59 C"
# parts_of_sentence = temperatures.split(":")
# print(parts_of_sentence)
# print(parts_of_sentence[-1])

# mars_temperatures = "The highest temperature on Mars is about -30 C"
# for item in mars_temperatures.split():
#     if item.isnumeric():
#         print(item)
#     elif item.startswith("-"):
#         print(item)
        
# REPLACING TEXT

# mars_temperatures = mars_temperatures.replace("C", "Celsius")
# print(mars_temperatures)

# JOINING TEST OF A LIST

# moon_facts = ["The Moon is drifting away from the Earth.", 'On average, the Moon is moving about 4cm every year.']
# print(' '.join(moon_facts))

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

                # PERCENT SIGN (%) FORMATTING
# mass_percent = "1/6"
# print("On the moon, you would weight about %s of your wight." % mass_percent) 

# print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

                # FORMAT METHOD
# mass_percent = '1/6'
# print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percent))

# mass_percentage = "1/6"
# print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

        # F-strings
# print(f"On the Moon, you would weigh about {round(1/6, 2)}% of your weight on Earth.")

# subject = "interesting facts about the moon"
# heading = f"{subject.title()}"
# print(heading)
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

  
    