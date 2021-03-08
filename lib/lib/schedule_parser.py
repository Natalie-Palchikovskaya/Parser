#-*- coding: utf-8 -*-
import re
import ast
import numpy as np
import pandas as pd
from check_file import file_exist
import re



file_path = r"C:\Users\Nat\Desktop\parser\input_data\test_schedule.inc"
data = file_exist(file_path)

def transform(keywords, parameters, input_file, output_file):
    """
    reads the input .inc-file and transforms it to .csv schedule
    :param keywords:
    :param parameters:
    :param input_file:
    :param output_file:
    :return:
    """
    return

def default_params_unpacking_in_line(parse_line):
    n =re.findall(r'([0-9])\*', parse_line)
    if len(n)!=0:
        for i in range(len(n)):
            parse_line = re.sub(n[i]+"\* ","DEFAULT "*int(n[i]), parse_line)
    return parse_line
# print(default_params_unpacking_in_line("'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"))

def read_schedule():
    return

def inspect_schedule():
    return



def clean_schedule(data):
    i = 0
    filt_data = []
    for line in data:
        line = re.sub('--[\w\D]+','', line)
        if not re.match(r'^\s*$', line):
            filt_data.append(line)
        i+=1
    return filt_data

# data1 = clean_schedule(data)
# # print(data1)
# print('\n'.join(data1))


def extract_keywords_blocks(data):
    dates_index = [i for i, d in enumerate(data) if d == 'DATES']
    blocks = []
    if dates_index[0]!=0:
        # dates.append(np.nan)
        blocks.append(data[:dates_index[0]-1])
    for i in range(1,len(dates_index)):
        blocks.append(data[dates_index[i-1]+1:dates_index[i]])
    blocks.append(data[dates_index[len(dates_index)-1]+1:])
    return  blocks



def extract_lines_from_keyword_block():
    return



def parse_keyword_block():
    return



def parse_keyword_COMPDAT_line(well_comp_line):
    well_comp_line = default_params_unpacking_in_line(well_comp_line)
    well_comp_line = re.sub('/', ' ', well_comp_line)
    well_comp_line = re.sub("'", ' ', well_comp_line)
    well_comp_line = well_comp_line.split()
    # print(type(well_comp_line))
    well_comp_line.insert(1, np.nan)
    return well_comp_line

# print(parse_keyword_COMPDAT_line("'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"))



def parse_keyword_DATE_line(current_date_line):
    current_date_line = re.sub('/+','', current_date_line)
    current_date_line = re.sub(r'\s$','', current_date_line)
    return current_date_line
# print(parse_keyword_DATE_line("01 JUN 2018 /"))



def parse_keyword_COMPDATL_line(well_comp_line):
    well_comp_line = default_params_unpacking_in_line(well_comp_line)
    well_comp_line = re.sub('/', ' ', well_comp_line)
    well_comp_line = re.sub("'", ' ', well_comp_line)
    return well_comp_line.split()
#print(parse_keyword_COMPDATL_line("'W3' 'LGR1' 10 10 2 2 OPEN 1* 1 2 1 3* 1.0918 /"))


def result_to_csv():
    return

def parse_schedule(clean_file_text, keywords_tuple = ("DATES", "COMPDAT", "COMPDATL")):
    result = []
    data = clean_file_text.split('\n')
    data = clean_schedule(data)
    blocks = extract_keywords_blocks(data)
    for block in blocks:
        print(block)
        dates_in_block = []
       #Ищем все даты в блоке, определенном по date
        for line in block:
            date = re.findall(r"[0-9]{2} [A-Z]{3} [0-9]{4}",line)
            if date!=[]:
                dates_in_block.append(date[0])


        if len(dates_in_block)==0:
             compdat_index = [i for i, d in enumerate(block) if d == 'COMPDAT' or d == 'COMPDATL']
             compdat_index.sort()
             for m in range(1,len(compdat_index)):
                 if block[compdat_index[m]] == "COMPDAT":
                     for l in range(compdat_index[m-1] + 1, compdat_index[m]-1):  # по строкам в блоке
                         line = default_params_unpacking_in_line(block[l])
                         line = parse_keyword_COMPDAT_line(line)
                         line.insert(0, np.nan)
                         result.append(line)


                     if m==len(compdat_index)-1:
                         l = compdat_index[len(compdat_index)-1] + 1
                         line = default_params_unpacking_in_line(block[l])
                         line = parse_keyword_COMPDAT_line(line)
                         line.insert(0, np.nan)
                         result.append(line)


                 if block[compdat_index[m]] == "COMPDATL":
                     for l in range(compdat_index[m - 1] + 1, compdat_index[m] - 1):  # по строкам в блоке
                         line = parse_keyword_COMPDATL_line(block[l])
                         line.insert(0, np.nan)
                         line = default_params_unpacking_in_line(str(line))
                         line.split()
                         result.append(line)

                     if m == len(compdat_index) - 1:
                         l = compdat_index[len(compdat_index)-1] + 1
                         line = parse_keyword_COMPDATL_line(block[l])
                         line.insert(0, np.nan)
                         line = default_params_unpacking_in_line(str(line))
                         line.split()
                         result.append(line)


        if len(dates_in_block) > 1:
            for i in range(len(dates_in_block)-1):
                result.append([dates_in_block[i], np.nan])

            date = dates_in_block[len(dates_in_block)-1]
            compdat_index = [i for i, d in enumerate(block) if d == 'COMPDAT' or d == 'COMPDATL']
            compdat_index.sort()
            if len(compdat_index)!=0:
                for m in range(len(compdat_index)):
                    print(block[compdat_index[m]])
                    if block[compdat_index[m]] == "COMPDAT":
                        for l in range(compdat_index[m] + 1, compdat_index[m-1] - 1):  # по строкам в блоке
                            line = default_params_unpacking_in_line(block[l])
                            line = parse_keyword_COMPDAT_line(line)
                            line.insert(0, date)
                            result.append(line)


                    elif block[compdat_index[m]] == "COMPDATL":
                        for l in range(compdat_index[m] + 1, compdat_index[m-1] - 1):  # по строкам в блоке
                            line = default_params_unpacking_in_line(block[l])
                            line = parse_keyword_COMPDATL_line(line)
                            line.insert(0, date)
                            result.append(line)

                        l = compdat_index[len(compdat_index) - 1] + 1
                        line = default_params_unpacking_in_line(block[l])
                        line = parse_keyword_COMPDATL_line(line)
                        line.insert(0, date)
                        result.append(line)
            else:
                result.append([date, np.nan])


        if len(dates_in_block) == 1:
            date = dates_in_block[0]
            compdat_index = [i for i, d in enumerate(block) if d == 'COMPDAT' or d == 'COMPDATL']
            compdat_index.sort()

            if len(compdat_index) == 1:
                m = 0
                if block[compdat_index[m]] == "COMPDAT":
                    for l in range(compdat_index[m] + 1, len(block)-1):  # по строкам в блоке
                        line = default_params_unpacking_in_line(block[l])
                        line = parse_keyword_COMPDAT_line(line)
                        line.insert(0, date)
                        result.append(line)


                if block[compdat_index[m]] == "COMPDATL":
                    for l in range(compdat_index[m - 1] + 1, compdat_index[m] - 1):  # по строкам в блоке
                        line = default_params_unpacking_in_line(block[l])
                        line = parse_keyword_COMPDATL_line(line)
                        line.insert(0, date)
                        result.append(line)

                    l = compdat_index[len(compdat_index) - 1] + 1
                    line = default_params_unpacking_in_line(block[l])
                    line = parse_keyword_COMPDATL_line(line)
                    line.insert(0, date)
                    result.append(line)

            elif len(compdat_index)>1:

                for m in range(1, len(compdat_index)):
                    if block[compdat_index[m-1]] == "COMPDAT":
                        for l in range(compdat_index[m - 1] + 1, compdat_index[m] - 1):  # по строкам в блоке
                            line = parse_keyword_COMPDAT_line(block[l])
                            line.insert(0, date)
                            line = default_params_unpacking_in_line(str(line))
                            line.split()
                            result.append(line)

                        l = compdat_index[len(compdat_index) - 1] + 1
                        line = parse_keyword_COMPDAT_line(block[l])
                        line.insert(0, date)
                        line = default_params_unpacking_in_line(str(line))
                        line.split()
                        result.append(line)

                    elif block[compdat_index[m]] == "COMPDATL":
                        for l in range(compdat_index[m - 1] + 1, compdat_index[m] - 1):  # по строкам в блоке
                            line = parse_keyword_COMPDATL_line(block[l])
                            line.insert(0, date)
                            line = default_params_unpacking_in_line(str(line))
                            line.split()
                            result.append(line)

                        l = compdat_index[len(compdat_index) - 1] + 1
                        line = parse_keyword_COMPDATL_line(block[l])
                        line.insert(0, date)
                        line = default_params_unpacking_in_line(str(line))
                        line.split()
                        result.append(line)


            else:
                result.append([date, np.nan])
    return result


clean_file = r"C:\Users\Nat\Desktop\Parser2\data\handled_schedule.inc"
with open(clean_file, "r", encoding="utf-8") as file:
    clean_file_text = file.read()

# res = parse_schedule(clean_file_text, keywords_tuple = ("DATES", "COMPDAT", "COMPDATL"))
# print("res")
# for i in range(len(res)):
#     print(res[i])
#     print()
# print(res)
