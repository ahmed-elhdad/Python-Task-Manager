def create_file(file_name,file_extention):
    with open(f'data/{file_name}.{file_extention}','x') as f:
        print(f'create file named f{file_name}.{file_extention}')