
class User:
    def __init__(self,id,name,tasks):
        self.id=id
        self.name=name
        self.tasks=tasks
    def log_in(array):
        name=input('Enter your Name: \n')
        password=input('Enter your Password: \n')
        for n in range(len(array)):
            if array[n]['name'] != name or array[n]['password']!= password:
                return name
            if array[n]['name'] == name or array[n]['password']== password:
                return False