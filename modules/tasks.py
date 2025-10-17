
from modules.user import User
from func.convert_from_json import convert_from_json
from func.getnererate_user_id import generate_user_id
from modules.user import User

global tasks

class Task:
    def __init__(self,id,title,description,created_at,endded_at,status):
        id=generate_user_id(10)
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
        if log_in==True:
            print("Feild to log in")
        else:
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
                    