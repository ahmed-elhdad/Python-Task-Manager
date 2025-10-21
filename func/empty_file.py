def empty_file(path):
    try:
        with open(path,'r+') as f:
            f.truncate(0)
    except :
        print("not Found File")