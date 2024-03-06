#Strings
######### ------------------  WORKING WITH STRINGS -----------------  ##########

# Using tripple quotations like a line breaker or text editor
# using ".tittle() to print initial in caps"

multiline = """
Facts about the Moon:
There is no atmosphere
There is no sound.
            """
print(multiline.title())

# --------------------------------------------------------

# SPLIT A STRING 

# saving it in a list.

temperatures = "this method helps separate the string at every space, like this. 9 38"
temperatures_list = temperatures.split()
print(temperatures_list)

# -------------------------------------------------------

# Finding and counting words in a string

print("Word" in "We are only trying to see if Python can find the Word in this string, if returns False is because is not here")
# ---------
words = ("""We are only trying to see if Python can find the Word in this string, if returns False is because is not here""".lower())
print(words.find("word"))
print(words.count("only"))
print(words.count("i"))

# --------------------------------------------------------

# CHECKING CONTENT

temperatures = "Mars Average Temperatures: -60 C And -59 C"
parts_of_sentence = temperatures.split(":")
print(parts_of_sentence)
print(parts_of_sentence[-1])

mars_temperatures = "The highest temperature on Mars is about -30 C"
for item in mars_temperatures.split():
    if item.isnumeric():
        print(item)
    elif item.startswith("-"):
        print(item)
        
# REPLACING TEXT

mars_temperatures = mars_temperatures.replace("C", "Celsius")
print(mars_temperatures)

# JOINING TEST OF A LIST

moon_facts = ["The Moon is drifting away from the Earth.", 'On average, the Moon is moving about 4cm every year.']
print(' '.join(moon_facts))