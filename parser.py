import os
file_path = r"C:\Users\Nat\Desktop\parser\test_schedule.inc"
if os.path.exists(file_path):
    print("Файл существует")
    file = open(file_path,"r", encoding="utf-8")
    data = file.read()
    print("Было прочитано:")
    print(data)
    file.close()
else:
    print("Файл не существует")