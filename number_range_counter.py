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
        number = int(input(f"Enter a number between 1 - 50 : "))
        if 1 <= int(number) <= 10:
            numbers_1_10 += 1
            numbers.append(int(number))
        elif 11 <= int(number) <= 20:
            numbers_11_20 += 1
            numbers.append(int(number))
        elif 21 <= int(number) <= 30:
            numbers_21_30 += 1
            numbers.append(int(number))
        elif 31 <= int(number) <= 40:
            numbers_31_40 += 1
            numbers.append(int(number))
        elif 41 <= int(number) <= 50:
            numbers_41_50 += 1 
            numbers.append(int(number))
        #Exits loop when number is more than 50 or a non number / digit is entered
        else:
            print(f"{'_'*50}\nNumber out of range, exiting...")
            break
    except ValueError:
        print(f"{'_'*50}\nInvalid input, exiting...")
        break
#Categorize numbers in different number ranges
number_inside_1_10 = [number for number in numbers if 1 <= int(number) <= 10]  
number_inside_11_20 = [number for number in numbers if 11 <= int(number) <= 20]  
number_inside_21_30 = [number for number in numbers if 21 <= int(number) <= 30]  
number_inside_31_40 = [number for number in numbers if 31 <= int(number) <= 40]  
number_inside_41_50 = [number for number in numbers if 41 <= int(number) <= 50]    
#Display how many times a number is entered within number ranges   
print(f"{'_'*50}\nNumbers count (1 - 10): {numbers_1_10}\nNumbers collection : {number_inside_1_10}")
print(f"{'_'*50}\nNumbers count (11 - 20): {numbers_11_20}\nNumbers collection : {number_inside_11_20}")
print(f"{'_'*50}\nNumbers count (21 - 30): {numbers_21_30}\nNumbers collection : {number_inside_21_30}")   
print(f"{'_'*50}\nNumbers count (31 - 40): {numbers_31_40}\nNumbers collection : {number_inside_31_40}")
print(f"{'_'*50}\nNumbers count (41 - 50): {numbers_41_50}\nNumbers collection : {number_inside_41_50}\n{'_'*50}")
