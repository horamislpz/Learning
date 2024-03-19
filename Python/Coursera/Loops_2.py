
line_number = 0
with open('C:\\Users\\horam\\Desktop\\Planned robust and comprehensive .txt') as file:
    for line in file:
        print('Line: ' + str(line_number) +' --> ' + str(line))
        line_number +=1