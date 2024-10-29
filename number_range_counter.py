#Initialize an empty list for numbers
numbers = []
#loop for the user input
while True:
    #prompts user to enter a number between 1 - 50
    try:
        number = int(input(f"{'-'*50}\nEnter a number between 1 - 50 : "))
    except ValueError:
        print(f"{'-'*50}\nInvalid input, exiting...")
        break
    
