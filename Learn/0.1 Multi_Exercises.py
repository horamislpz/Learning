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

from math import ceil, floor

first_planet_input = input("Enter the distance from the sun for the first planet in km\n")
second_planet_input = input("Enter the distance from the sun for the second planet in km\n")

# converting from string to int

first_planet = float(first_planet_input)
second_planet = float(second_planet_input)

# calculation

distance_km = (second_planet - first_planet)
print('Distance = ' + str(ceil(distance_km)))
print('Distance_float = ' + str(distance_km))

# -----------------------------------------------------------------


