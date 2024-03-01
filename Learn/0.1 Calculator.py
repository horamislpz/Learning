# Calculator

while True:
    operation = str(input("Type of operation: + = Sum, - = Minus and * = Factor\n"))
    if operation == '+':
        first_number = float(input("\nType the first number: \n"))
        second_number = float(input("\nType the second number: \n"))
        result = first_number + second_number
        print("THE SUM OF THE TWO NUMBERS PROVIDED = " + str(result))
        break 
    else :{
    print("YOU MUST INDICATE THE TYPE OF OPERATION\n")      
    }