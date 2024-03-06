                # WHILE AND FOR LOOPS
        # WHILE

person_name = ''
while person_name=='':
    print('Please, complete the information below')
    first_name = input('First Name: \n')
    last_name = input('Last Name: \n')
    person_name = first_name + last_name

        ## Creating list with user inputs

names = ''
name_list = [] 

while names.lower() != 'done':
    if names:
        name_list.append(names)
    names = input("Please provide the list of names or 'done' when done\n")
    print(name_list)


        ## FOR

countdown = [4,3,2,1,0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

# Waiting a second for every iteration
from time import sleep
countdown = [4,3,2,1,0]
for number in countdown:
    print(number)
    sleep(1)
print("Blast off!! 🚀")