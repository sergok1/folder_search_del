import os

def delete_empty_folder(folder_name):
    home_dir = os.environ['USERPROFILE']
    folder_path = os.path.join(home_dir, folder_name)

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        if len(os.listdir(folder_path)) == 0:
            os.rmdir(folder_path)
            print(f"Папка {folder_name} успешно удалена")
        else:
            print(f"Папка {folder_name} не пустая")
    else:
        print(f"Папка {folder_name} не найдена")

folder_name = input("Введите имя папки: ")
delete_empty_folder(folder_name)
