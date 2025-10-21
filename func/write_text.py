from func.convert_to_json import convert_to_json

def write_text(file,mode,txt):
    try:
        with open(file,mode) as f:
            txt=convert_to_json(txt)
            f.write(txt)
    except ValueError:
        print("No text to write")