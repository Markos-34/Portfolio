# Initialize variables for the menu choice and the final answer
menu_choice = 0 
answer = 0


# Start a loop that continues until the user chooses to exit (option 7)
while menu_choice != 7:
    # Display the main menu
    print("**********Unit Converter**********\n")
    menu_choice = int(input("""1)Kilometers to Miles\n
                            2)Miles to Kilometers\n
                            3)Celsius to Fahrenheit\n
                            4)Fahrenheit to Celsius\n
                            5)Kilograms to Pounds\n
                            6)Pounds to Kilograms\n
                            7)Exit\n"""))# Prompt the user to choose a conversion type
    # If the user chooses to exit, break the loop
    if menu_choice == 7:
        break
    
    # Conversion: Kilometers to Miles
    if menu_choice == 1:
        kilometers = float(input("Enter Kilometers: "))
        answer = kilometers *  0.62137
        print(answer)
        
    # Conversion: Miles to Kilometers
    elif menu_choice == 2:
        miles = float(input("Enter Miles: "))
        answer = miles * 1.60934
        print(answer)
        
    # Conversion: Celsius to Fahrenheit
    elif menu_choice == 3:
        celsius = float(input("Enter Celsius: "))
        answer = (celsius*(9/5)) + 32  # Formula: (°C × 9/5) + 32 = °F
        print(answer)
        
    # Conversion: Fahrenheit to Celsius    
    elif menu_choice == 4:
        fahrenheit = float(input("Enter Fahrenheit: "))
        answer = (fahrenheit-32) * (5/9) # Formula: (°F − 32) × 5/9 = °C    
        print(answer)
        
    # Conversion: Kilograms to Pounds   
    elif menu_choice == 5:
        kilograms = float(input("Enter Kilograms: "))
        answer = kilograms * 2.2
        print(answer)
        
    # Conversion: Pounds to Kilograms    
    elif menu_choice == 6:
        pounds = float(input("Enter Pounds: "))
        answer = pounds/2.20462
        print(answer)