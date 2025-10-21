
class User:
    def __init__(self,id,name,tasks):
        self.id=id
        self.name=name
        self.tasks=tasks
    def log_in(array):
        print("Log in: ")
        name=input('Enter your Name: \n').strip()
        password=input('Enter your Password: \n').strip()
        for user in array:
            print(array)
            if user['name'].lower() == name.lower():
                if user['password'] == password:
                    return user
                
            else:
                return 'not found'
        return 'not found'