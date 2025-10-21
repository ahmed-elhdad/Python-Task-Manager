import json

def convert_to_json(txt):
    try:
        converted_txt=json.dumps(txt,indent=4)
        return converted_txt
    except Exception as e:
        print("Error convert from python to json: ",e)