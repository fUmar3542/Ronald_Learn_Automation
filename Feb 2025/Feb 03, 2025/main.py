# ###############################################################################
#
# To-Do List Application
#
# Build a to-do list program that:
# - Allows users to add, remove, and mark tasks as complete.
# - Displays tasks with their status (completed or pending).
# - Bonus: Add an option to prioritize tasks and sort them by priority.
#
# ###############################################################################
#
# # Input
#
# To-Do List Options:
# 1. Add a task
# 2. Remove a task
# 3. Mark a task as complete
# 4. View all tasks
# 5. Exit
#
# Enter your choice: 1
# Enter the task description: Finish the project report
# Enter the task priority (High/Medium/Low): High
#
#
# # Output
#
# Task added successfully!
#
# ###############################################################################
#
# # Input
#
# To-Do List Options:
# 1. Add a task
# 2. Remove a task
# 3. Mark a task as complete
# 4. View all tasks
# 5. Exit
#
# Enter your choice: 4
#
#
# # Output
#
# Your To-Do List:
# 1. [ ] Finish the project report (Priority: High)
# 2. [ ] Buy groceries (Priority: Medium)
#
#
# ###############################################################################
#
# # Input
#
# To-Do List Options:
# 1. Add a task
# 2. Remove a task
# 3. Mark a task as complete
# 4. View all tasks
# 5. Exit
#
# Enter your choice: 3
# Enter the task number to mark as complete: 1
#
#
# # Output
#
# Task 'Finish the project report' marked as complete!
#
# ###############################################################################
#
# # Input
#
# To-Do List Options:
# 1. Add a task
# 2. Remove a task
# 3. Mark a task as complete
# 4. View all tasks
# 5. Exit
#
# Enter your choice: 4
#
#
# # Output
#
# Your To-Do List:
# 1. [Done] Finish the project report (Priority: High)
# 2. [ ] Buy groceries (Priority: Medium)

task_formatted = 0
user_choice = 0
priority_number = {"Low": 1, "Medium": 2, "High": 3}

task_list = [{"Status": "Complete","Task": "read","Priority": "High"},
{"Status": "In Progress","Task": "write","Priority": "Medium"},
{"Status": "Complete","Task": "run","Priority": "High"},
{"Status": "In Progress","Task": "paint","Priority": "Low"}]

sorted_task_list = []

check = False
priority = 0
status = 0
task = 0
priority_list = ["high","medium","low"]
priority_choice = 0
count = 1
remove_task_choice = 0
index_list = []

while True:
    try:
        user_choice = int(input("\nLibrary System Options:\n 1. Add a task\n 2. Remove a task\n 3. Mark a task as complete\n 4. View all tasks\n 5. Exit \n\nEnter your choice: "))
        print("")
    except:
        print("Error: invalid value entered. Only options 1-5 are available.")
    if user_choice == 1:
        try:
            task = input("Enter the task description: ").strip()
            if task.isalnum():
                while True:
                    priority = input("Enter the task priority (High/Medium/Low): ").lower()
                    if priority in priority_list:
                        priority = priority.capitalize()
                        status = "In Progress"
                        task_list.append({"Status": status,"Task": task.lower(),"Priority": priority})
                        print(f"You have successfully added '{task}' to the to-do-list")
                        break
                    else:
                        print("Error: please enter high, medium or low.")
            else:
                print("Error: must enter a value")
        except:
            print("Error: invalid entry.")
    elif user_choice == 2:
        index = 0
        for j in range(len(task_list)):
            index = index + 1
            index_list.append(index)
            for i in range(0, len(task_list) - j - 1):
                if task_list[i]["Status"] == "Completed" and task_list[i + 1]["Status"] == "Completed":
                    pass
                elif task_list[i]["Status"] != "Completed" and task_list[i + 1]["Status"] == "Completed":
                    task_list[i], task_list[i + 1] = task_list[i + 1], task_list[i]
                elif priority_number[task_list[i]["Priority"]] < priority_number[task_list[i + 1]["Priority"]]:
                    task_list[i], task_list[i + 1] = task_list[i + 1], task_list[i]
        for index, x in enumerate(task_list):
            print(f"{index + 1}. Status: {x["Status"]} | Task: {x["Task"]} | Priority: {x["Priority"]}\n")
        while True:
            try:
                remove_task_choice = int(input("Which task would you like to remove? Enter task number: "))
                remove_task_choice = remove_task_choice - 1
                if remove_task_choice < len(index_list):
                    task_display = task_list[remove_task_choice]["Task"]
                    del task_list[remove_task_choice]
                    print(f"You have successfully removed '{task_display}' from your to-do-list")
                    break
                else:
                    print("Error: option not available. Try again.")
            except:
                print("Error: invalid number entered. Try again")
    elif user_choice == 3:
        index = 0
        for j in range(len(task_list)):
            index = index + 1
            index_list.append(index)
            for i in range(0, len(task_list) - j - 1):
                if task_list[i]["Status"] == "Completed" and task_list[i + 1]["Status"] == "Completed":
                    pass
                elif task_list[i]["Status"] != "Completed" and task_list[i + 1]["Status"] == "Completed":
                    task_list[i], task_list[i + 1] = task_list[i + 1], task_list[i]
                elif priority_number[task_list[i]["Priority"]] < priority_number[task_list[i + 1]["Priority"]]:
                    task_list[i], task_list[i + 1] = task_list[i + 1], task_list[i]
        for index, x in enumerate(task_list):
            print(f"{index + 1}. Status: {x["Status"]} | Task: {x["Task"]} | Priority: {x["Priority"]}\n")
        while True:
            try:
                mark_task_complete_choice = int(input("Which task you would you like to mark as complete? Enter task number: "))
                mark_task_complete_choice = mark_task_complete_choice - 1
                if mark_task_complete_choice < len(index_list):
                    task_list[mark_task_complete_choice]["Status"] = "Complete"
                    print(task_list[mark_task_complete_choice])
                    print(f"You have successfully marked '{task_list[mark_task_complete_choice]["Task"]}' as complete")
                    break
                else:
                    print("Error: option not available. Try again.")
            except:
                print("Error: invalid number entered. Try again")
    elif user_choice == 4:
        index = 0
        for j in range(len(task_list)):
            index = index + 1
            index_list.append(index)
            for i in range(0, len(task_list) - j - 1):
                if task_list[i]["Status"] == "Completed" and task_list[i + 1]["Status"] == "Completed":
                    pass
                elif task_list[i]["Status"] != "Completed" and task_list[i + 1]["Status"] == "Completed":
                    task_list[i], task_list[i + 1] = task_list[i + 1], task_list[i]
                elif priority_number[task_list[i]["Priority"]] < priority_number[task_list[i + 1]["Priority"]]:
                    task_list[i], task_list[i + 1] = task_list[i + 1], task_list[i]
        for index, x in enumerate(task_list):
            print(f"{index + 1}. Status: {x["Status"]} | Task: {x["Task"]} | Priority: {x["Priority"]}\n")


# Enter the task description: Finish the project report
# Enter the task priority (High/Medium/Low): High
