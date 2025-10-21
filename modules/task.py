
from modules.user import User
from func.convert_from_json import convert_from_json
from func.genererate_user_id import generate_user_id
from modules.user import User
import datetime

global tasks

class Task:
    def __init__(self,id,title,description,created_at,endded_at,status):
        id=generate_user_id(10)
        self.id=id
        self.title=title
        self.description=description
        self.created_at=created_at
        self.endded_at=endded_at
        self.status=status
    def show_tasks(users):
        users_data=convert_from_json('data/users.json')
        users=users_data
        log_in=User.log_in(users)
        print(log_in)
        if log_in=='found':
            print("Logged In")
            user_data = convert_from_json(f'data/{log_in}.json')
            for i in (user_data['tasks']):
                print("For loop")
                print(f"""
TASK {i}: 
Title: {[i].name}
Desctiption: {[i].description}
Created_at: {[i].created_at}
Created_at: {[i].created_at}
Status: {[i].status}
    """)
        else:
            print("Feild to log in")
            return

    def  add_task():
        users_data=convert_from_json('data/users.json')
        users=users_data
        user_status =  User.log_in(users)
        if user_status == 'not found':
            print("❌ not Found")
        else:
            print("✅ Found")
        # if user_status == 'not found':
        #     print('not found user')
        #     return 
        # else:
            print("User Logged")
            id=generate_user_id(7)
            title=input("Enter task's title: \n")
            desc=input("Enter task's description: \n")
            created_at=datetime.datetime.now().isoformat()
            endded_at=input("Enter task's endded at: \n")
            status='pending'
            if title == '' or desc=='' or endded_at=='':
                print("Valid data entry ^^")
                return
            print("Adding...")
            new_task=Task(id,title,desc,str(created_at),endded_at,status)
            print("New Task: ",new_task.__dict__)
            global tasks
            tasks=[]
            tasks.append(new_task.__dict__)
            print(tasks)
            from func.write_text import write_text
            user=User(id,user_status,tasks)
            from func.empty_file import empty_file
            empty_file(f'data/{user_status}.json')
            print(f'data/{user_status}.json')
            print(type(user))
            write_text(f'data/{user_status}.json','w',user.__dict__)