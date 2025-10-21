from func.genererate_user_id import generate_user_id
from func.convert_from_json import convert_from_json
def check_exit_user(name,id):
    converted_data=convert_from_json('data/users.json')
    if converted_data is None:
        return
    if len(converted_data)==0 or converted_data is None:
        print("fdfdsaf")
        return
    else:
            
        for x in converted_data:
            if x['id']==id:
                generate_user_id(10)
            elif x['name'].lower() == name.lower():
                print('exit user')
                return True
            else:
                return False