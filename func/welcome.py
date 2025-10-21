import os
from modules.users import Users
from modules.users import users
from modules.task import Task
def welcome():
    print(users,"""
          
1- Press 1 to create account or login.
2- Press 2 to show your tasks.
3- Press 3 to add task.
4- Press 4 to check true task or remove.
5- Press 5 to remove task.
6- Press 6 to exit
""")
    enter = int(input("Enter Num: \n"))
    while enter is None:
        print('Enter Num: \n')
    if enter == 1:Users.add_user()
    if enter == 2:Task.show_tasks(users)
    if enter == 3:Task.add_task()