import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.R_OK) and os.access(path, os.W_OK):
            os.remove(path)
            print('file deleted')
        else:
            print(f"Нет доступа для удаления '{path}'.")
    else:
        print(f"Файл по пути {path} не существует.")

file_path = input("path = ")
delete_file(file_path)