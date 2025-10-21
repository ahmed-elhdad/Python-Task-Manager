users=[]

def get_users_data(file,mode):
    try:
        with open(file,mode)as f:
            data=f.read()
            users.append(data)
            return data
    except Exception as e:
        print("Error")