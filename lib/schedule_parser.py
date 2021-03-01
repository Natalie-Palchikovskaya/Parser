#-*- coding: utf-8 -*-
import re
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
print(default_params_unpacking_in_line("'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"))

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



def parse_schedule():

    return

def extract_keywords_blocks():
    return


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


