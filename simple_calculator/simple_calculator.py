menu_choice = '0'
answer = '0'

while menu_choice != '6':
    menu_choice = '0'
    #Menu
    menu_choice = input("""**********MENU**********\n
      1)Addition\n
      2)Substraction\n
      3)Multiplication\n
      4)Division\n
      5)Power\n
      6)Exit\n""")
    
    if menu_choice == '6':
        break
    
    number_one = input("Please enter the first number: ")
    number_two = input("\nPlease enter the econd number: ")
    
    #Addition
    if menu_choice == '1':
        answer = int(number_one) + int(number_two)
        print(answer)
    #Substraction
    elif menu_choice == '2':
        answer = int(number_one) - int(number_two)
        print(answer)
    #Multiplication
    elif menu_choice == '3':
        answer = int(number_one) * int(number_two)
        print(answer)
    #Division
    elif menu_choice == '4':
        if number_two == '0':
            print("You can't divede with zero!")
        else:
            answer = int(number_one) / int(number_two)
            print(answer)
    #Power
    elif menu_choice == '5':
        answer = int(number_one) ** int(number_two)
        print(answer)
        