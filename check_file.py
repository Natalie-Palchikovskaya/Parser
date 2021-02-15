import os
file_path = r"C:\Users\Nat\Desktop\parser\\input_data\test_schedule.inc"

def file_exist(file_path):
    if os.path.exists(file_path):
        # print("Файл существует")
        # file = open(file_path,"r", encoding="utf-8")
        with open(file_path,"r", encoding="utf-8") as f:
            data = f.read().split('\n')
        return data
    else:
        print("Файл не существует")

data =file_exist(file_path)



