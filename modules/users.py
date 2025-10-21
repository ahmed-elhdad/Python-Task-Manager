from func.check_exit import check_exit_user
from func.genererate_user_id import generate_user_id
from func.get_data import users
from func.empty_file import empty_file
from func.write_text import write_text
from func.convert_from_json import convert_from_json
from func.create_file import create_file

class Users:
    def __init__(self,name,password,id):
        self.id=id
        self.name=name
        self.password=password
    def add_user():
        convert_from_json('data/users.json')
        id=generate_user_id(10)
        name=input('Enter your name: \n')
        password=input('Enter your password: \n')
        while name=='' or password=='':
            input("Enter your name: \n")
            input("Enter your password: \n")
            if name is not None or password is not None:
                break

        if check_exit_user(name,id) == True:
            print("valid data Entry ^^ ")
            return
        new_user=Users(name,password,id)
        converted_from_json=convert_from_json('data/users.json')
        if convert_from_json == 'nothing to convert':
            return
        users=list(converted_from_json)
        users.append(new_user.__dict__)
        create_file(name,'json')
        from modules.user import User
        user=User(id,name,[])
        write_text(f'data/{name}.json','w',user.__dict__)
        empty_file('data/users.json')
        if len(users) > 1:
            write_text('data/users.json','w',users)
        else:
            write_text('data/users.json','w',users)