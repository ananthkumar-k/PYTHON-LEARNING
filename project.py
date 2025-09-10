
# #EXPENSE TRACKER
# expenses = []

# while True:
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Total Expenses")
#     print("4. Exit")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         name = input("Enter expense name: ")
#         amount = float(input("Enter amount: "))
#         expenses.append((name, amount))
#     elif choice == "2":
#         for e in expenses:
#             print(e[0], e[1])
#     elif choice == "3":
#         total = 0
#         for e in expenses:
#             total += e[1]
#         print("Total:", total)
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice")


# #TO-DO LiST

# tasks = []
# while True:
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Remove Task")
#     print("4. Exit")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         task = input("Enter task: ")
#         tasks.append(task)
#     elif choice == "2":
#         for i, t in enumerate(tasks):
#             print(i + 1, t)
#     elif choice == "3":
#         num = int(input("Enter task number: "))
#         if 0 < num <= len(tasks):
#             tasks.pop(num - 1)
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice")

