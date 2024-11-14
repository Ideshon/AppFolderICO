# Folder ICO

Положить файл в папку с папками, на которых нужно сменить ярлык и запустить.
Программа сканирует папки и прописывает ярлык в desktop.ini на основе совпадения имени папки и имени exe.
_Строка ярлыка добавляется в конец файла desktop.ini._

## Рекомендации по использованию программы:

**Запуск от имени администратора:**
Чтобы избежать проблем с правами доступа при установке атрибутов или записи файлов, рекомендуется запускать программу от имени администратора.

**Проверка лог-файла:**
После выполнения программы ознакомьтесь с log.txt, чтобы увидеть подробную информацию о том, что было сделано для каждой папки.
Обновление отображения:

Если изменения не видны сразу, попробуйте **обновить вид папки** или перезапустить проводник Windows.

## Возможные ошибки и их обработка:

**Недостаточно прав доступа:**

* Симптомы: Ошибки при чтении или записи файлов, установка атрибутов не выполняется.
* Решение: Программа выводит сообщение об ошибке и рекомендует запустить ее от имени администратора.

**Файл desktop.ini поврежден или имеет неправильный формат:**

* Симптомы: Ошибка при чтении файла, программа не может найти нужную строку.
* Решение: Программа попытается обновить или перезаписать файл, выводя соответствующее сообщение.

**Путь к файлам слишком длинный:**

* Симптомы: Ошибки при доступе к файлам или папкам.
* Решение: Программа выводит сообщение об ошибке с описанием проблемы.

**Отсутствие .exe файлов в папке:**

* Симптомы: Программа сообщает, что .exe файлы не найдены.
* Решение: Это ожидаемое поведение, программа информирует пользователя об этом.

**Исключения при работе с файлами:**

* Симптомы: Непредвиденные ошибки, такие как FileNotFoundError, PermissionError и т.д.
* Решение: Все операции ввода-вывода обернуты в try-except, и программа выводит подробное сообщение об ошибке.

# Folder ICO

Put the file in a folder with folders where you need to change the shortcut and run.
The program scans folders and prescribes a shortcut in desktop.ini based on the coincidence of the folder name and the exe name.
_ The shortcut string is appended to the end of the desktop.ini file._

## Recommendations for using the program:

**Run as an administrator:**
To avoid problems with access rights when setting attributes or writing files, it is recommended to run the program as an administrator.

**Checking the log file:**
After completing the program, familiarize yourself with log.txt to see the details of what has been done for each folder.
Updating the display:

If the changes are not immediately visible, try **updating the folder view** or restarting Windows Explorer.

## Possible errors and their handling:

**Insufficient access rights:**

* Symptoms: Errors when reading or writing files, attribute setting is not performed.
* Solution: The program displays an error message and recommends running it as an administrator.

**The desktop.ini file is corrupted or has an incorrect format:**

* Symptoms: Error when reading the file, the program cannot find the desired line.
* Solution: The program will try to update or overwrite the file by displaying the appropriate message.

**The file path is too long:**

* Symptoms: Errors when accessing files or folders.
* Solution: The program displays an error message describing the problem.

** Absence .exe files in the folder:**

* Symptoms: The program reports that .exe files were not found.
* Solution: This is the expected behavior, the program informs the user about it.

**Exceptions when working with files:**

* Symptoms: Unexpected errors such as FileNotFoundError, PermissionError, etc.
* Solution: All I/O operations are wrapped in try-except, and the program outputs a detailed error message.