#packages
from datetime import datetime

#List of tasks
tasks = []
#menu choice to go throw the loop for the first time
menu_choice = 0
#Running till user enter 4 to exit
while menu_choice != '4':
    #Menu for the user to see the choices and chosse
    menu_choice = input("""**********MENU**********\n
      1)Add Tasks\n
      2)Remove Tasks\n
      3)List Tasks\n
      4)Exit\n""")
    
    if menu_choice == '1':#if user enter 1, program adds a tasks
        tasks_name = input("Please enter name for a Task: ")
        #Run till you put the valid format
        while True:
            tasks_date = input("\nPlease enter a date for your Task (dd/mm/yy): ")
            try:
                due_date = datetime.strptime(tasks_date, "%d/%m/%y")
                break
            except ValueError:
                print("Invalid date format. Please try again!!")
                
        task = {"name": tasks_name, "due": due_date}#make the inputs into a dictionary and then save the dictionary into the list
        tasks.append(task)
        
        
    elif menu_choice == '2':#if user enter 2, program remove a task
        remove_task = input("Please enter what task to remove: ")
        #search for the task and if it found it the program will remove it
        for search_task in tasks:
            if remove_task == search_task["name"]:
                tasks.remove(search_task)
                print(f"Task Remove: {remove_task}")
                break
            else:
                print("Task not found!")
        
    elif menu_choice == '3':#if user enter 3, program prints tasks
        sorted_tasks = sorted(tasks, key=lambda task: task["due"])#short the list with due time
        for task in sorted_tasks:
            formatted_date = task["due"].strftime("%d/%m/%y")
            print(f"{task['name']}: {formatted_date}")
    