"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os


def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfold_paths(folder_path) -> list:
    subfold_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfold_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(f'Moving {file_name} to {ext_list[dict_key_int][0]}\n')
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfold_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == '__main__':
    extensions = {
        'video': ['mp4', 'mpg', 'mpeg', 'm4v'],
        'data': ['json', 'csv', 'dat', 'db', 'log', 'mdb', 'xml'],
        'audio': ['mp3', 'mpa', 'wma', 'wpl', 'cda'],
        'image': ['jpg', 'png', 'bmp', 'ico', 'jpeg', 'svg', 'img'],
        'archive': ['zip', 'rar', '7z', 'z', 'pkg', 'deb'],
        'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
        'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],
        'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],
        'gif': ['gif'], 'exe': ['exe'], 'bat': ['bat'], 'apk': ['apk']
    }

    # main_path = r'E:\GB\PY_projects\Python_deep\lesson_7\datas'
    main_path = input("Enter folder path for sort: ")
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)















