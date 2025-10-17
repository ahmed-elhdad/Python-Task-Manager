import json
def convert_from_json(path):
    try:
        with open(path,'r')as f:
                data_converted=json.loads(f.read())
                return data_converted
    except Exception as e:
            return "nothing to convert: ",e