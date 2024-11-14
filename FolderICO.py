import os
import ctypes


def main():
    current_dir = os.getcwd()
    # Получаем список папок в текущей директории
    folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]

    folder_statuses = []  # Список для хранения статуса каждой папки

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        status = None  # Инициализируем статус для этой папки
        try:
            # Ищем .exe файлы в папке и её подпапках
            exe_files = []
            for root, dirs, files in os.walk(folder_path):
                for filename in files:
                    if filename.lower().endswith('.exe'):
                        exe_files.append(os.path.join(root, filename))
            if not exe_files:
                status = f"Не найден .exe файл для папки: {folder}"
                folder_statuses.append((folder, status))
                print(status)
                continue
            # Проверяем совпадение названий .exe файлов с названием папки
            matched_exe = None
            folder_name = os.path.basename(folder).lower()
            for exe_file in exe_files:
                exe_name = os.path.splitext(os.path.basename(exe_file))[0].lower()
                if folder_name in exe_name or exe_name in folder_name:
                    matched_exe = exe_file
                    match_type = "Найдено совпадение по имени"
                    break
            # Если совпадение не найдено, используем первый .exe файл
            if matched_exe is None:
                matched_exe = exe_files[0]
                match_type = "Использован первый найденный .exe"
            desktop_ini_path = os.path.join(folder_path, 'desktop.ini')
            icon_line = f'IconResource={matched_exe},0'
            need_to_write = True
            if os.path.exists(desktop_ini_path):
                try:
                    with open(desktop_ini_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    has_icon_line = False
                    for i, line in enumerate(lines):
                        if line.strip().startswith('IconResource='):
                            has_icon_line = True
                            if line.strip() != icon_line:
                                lines[i] = f'{icon_line}\n'
                                need_to_write = True
                            else:
                                need_to_write = False
                            break
                    if not has_icon_line:
                        lines.append(f'{icon_line}\n')
                        need_to_write = True
                    if need_to_write:
                        with open(desktop_ini_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        status = f"Обновлен ярлык для папки: {folder} ({match_type})"
                    else:
                        status = f"Ярлык уже установлен для папки: {folder}"
                except Exception as e:
                    status = f"Ошибка при чтении/записи desktop.ini в папке: {folder} - {e}"
            else:
                try:
                    # Записываем в desktop.ini
                    with open(desktop_ini_path, 'w', encoding='utf-8') as f:
                        f.write('[.ShellClassInfo]\n')
                        f.write(f'{icon_line}\n')
                    status = f"Установлен ярлык для папки: {folder} ({match_type})"
                except Exception as e:
                    status = f"Ошибка при создании desktop.ini в папке: {folder} - {e}"
            # Устанавливаем атрибуты для desktop.ini
            set_file_attributes(desktop_ini_path)
            # Устанавливаем атрибуты для папки
            set_folder_attributes(folder_path)
        except Exception as e:
            status = f"Ошибка при обработке папки: {folder} - {e}"
        folder_statuses.append((folder, status))
        print(status)

    # Записываем статусы в лог-файл
    try:
        with open("ICOlog.txt", "w", encoding="utf-8") as log_file:
            log_file.write("Статус папок после выполнения:\n")
            for folder, status in folder_statuses:
                log_file.write(f"{folder}: {status}\n")
        print("\nСтатус папок после выполнения записан в ICOlog.txt")
    except Exception as e:
        print(f"Ошибка при записи в лог-файл: {e}")
    input("\nНажмите Enter, чтобы выйти...")


def set_file_attributes(file_path):
    try:
        FILE_ATTRIBUTE_HIDDEN = 0x02
        FILE_ATTRIBUTE_SYSTEM = 0x04
        attributes = FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM
        ret = ctypes.windll.kernel32.SetFileAttributesW(file_path, attributes)
        if not ret:
            print(f"Не удалось установить атрибуты для файла: {file_path}. Возможно, требуются права администратора.")
    except Exception as e:
        print(f"Ошибка при установке атрибутов для файла: {file_path} - {e}")


def set_folder_attributes(folder_path):
    try:
        FILE_ATTRIBUTE_SYSTEM = 0x04
        attributes = ctypes.windll.kernel32.GetFileAttributesW(folder_path)
        if attributes == -1:
            print(f"Не удалось получить атрибуты для папки: {folder_path}. Возможно, требуются права администратора.")
            return
        ret = ctypes.windll.kernel32.SetFileAttributesW(folder_path, attributes | FILE_ATTRIBUTE_SYSTEM)
        if not ret:
            print(f"Не удалось установить атрибуты для папки: {folder_path}. Возможно, требуются права администратора.")
    except Exception as e:
        print(f"Ошибка при установке атрибутов для папки: {folder_path} - {e}")


if __name__ == "__main__":
    main()
