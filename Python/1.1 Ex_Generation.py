    #Exercise to determine the generation a person was born
    
birth_year = int(input("Please, enter the year you were born\n"))

if birth_year >= 2013:
    print("You are a member of Gen Alpha")
elif birth_year >= 1997:
    print("You are a member of Gen Z")
elif birth_year >= 1981:
    print("You are a Millenial")
elif birth_year >= 1965:
    print("You are a member of Generation X")
elif birth_year >= 1946:
    print("You are a Baby Boomer")
else:
    print("Error. Please enter a four digit year, 1946 or later.")