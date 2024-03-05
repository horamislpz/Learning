            # Dynamic Dictionaries
            
# To print every Key in a Dictionary

rainfall = {
    'november'.title() : 3.4,
    'december': 2.634,
    'january' : 8.956,
    'february' : 0.769,
    'march' : 6.1349,
    'january' : 1.93,
}
for key in rainfall.keys():
    print(f'{key.title()}:{rainfall[key]} cm')
print('---------------------------------------------\n')

# Determine if a key exists in a dictionary

if 'may' in rainfall:
    rainfall['may'] = 9.8
else:
    rainfall.update({'may': 9.8})
# print(rainfall)


if 'may' in rainfall:
    rainfall['may'] = round(rainfall['may'] + 156.9/3, 2)
# print(rainfall)

# Retreiving all the values in the dictionary

total_rainfall = 0.00
to100_rainfall = 0.00

for value in rainfall.values():
    total_rainfall = total_rainfall + value #Sum every key value in the dictionary adding it to the same variable
print(f'\nThere was {round(total_rainfall, 2)} cm in the las quarter.')

if total_rainfall <= 100:
    to100_rainfall = 100 - total_rainfall
print(f'Total rainfall: {round(total_rainfall,3)} cm. {round(to100_rainfall,4)} cm of rain to reach the top.\n')

# -----------------------

    # Exercise 'Average'

months_count = len(rainfall.keys())
average_month = 0

print('The sum of rainfall of all months is:', round(total_rainfall, 3), "")
average = total_rainfall / months_count
print('In each month theres an average rainfall of: ', '{:.4f}'.format(round(average, 4)), '\n')
                            # With 'format' we can print trailing zeros.
                            # '{:.4f}.format()' --> 4 = number of decimals
                            
