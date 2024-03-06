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


# More numbers exercise
# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# bus_weight = 124054

# print('On Earth, a double-checker bus weighs', bus_weight, 'N')
# print('On Mars, a double-decker bus weighs ', bus_weight*gravity_on_planets[1], 'N')
# print('The lightest a bus would be in solar system is ', bus_weight * min(gravity_on_planets), 'N')
# print('The heaviest a bus would be in solar system is ', bus_weight * max(gravity_on_planets), 'N')

# --------------------------------------------------------------



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

  
    