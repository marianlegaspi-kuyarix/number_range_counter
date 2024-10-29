#Initialize an empty list for numbers
numbers = []
#Initialize value for number ranges
numbers_1_10 = 0
numbers_11_20 = 0
numbers_21_30 = 0
numbers_31_40 = 0
numbers_41_50 = 0
#loop for the user input
while True:
    #prompts user to enter a number between 1 - 50
    try:
        number = int(input(f"{'-'*50}\nEnter a number between 1 - 50 : "))
        if 1 <= int(number) <= 10:
            numbers_1_10 += 1
            numbers.append(int(number))
        elif 11 <= int(number) <= 20:
            numbers_11_20 += 1
        elif 21 <= int(number) <= 30:
            numbers_21_30 += 1
        elif 31 <= int(number) <= 40:
            numbers_31_40 += 1
        elif 41 <= int(number) <= 50:
            numbers_41_50 += 1 
        #Exits loop when number is more than 50 or a non number / digit is entered
        else:
            print(f"{'-'*50}\nNumber out of range, exiting...")
            break
    except ValueError:
        print(f"{'-'*50}\nInvalid input, exiting...")
        break
#Categorize numbers in different number ranges
number_inside_1_10 = [number for number in numbers if 1 <= int(number) <= 10]    
#Display how many times a number is entered within number ranges   
print(f"{'-'*50}\nNumbers count (1 - 10): {numbers_1_10}\nNumbers collection : {number_inside_1_10}")
print(f"{'-'*50}\nNumbers count (11 - 20): {numbers_11_20}")
print(f"{'-'*50}\nNumbers count (21 - 30): {numbers_21_30}")   
print(f"{'-'*50}\nNumbers count (31 - 40): {numbers_31_40}")
print(f"{'-'*50}\nNumbers count (41 - 50): {numbers_41_50}")
