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


def read_schedule():
    return

def inspect_schedule():
    return

def clean_schedule(data):
    i = 0
    for line in data:
        line = re.sub('--[\w\D]+',' ', line)
        # line= re.sub(r'^[\s+\t+]', ' ', line)
        data[i] = line
        i+=1
    data.remove(' ') #??
    return data

data1 = clean_schedule(data)
print(data1)
print('\n'.join(data1))



def parse_schedule():

    return

def extract_keywords_blocks():
    return


def extract_lines_from_keyword_block():
    return



def parse_keyword_block():
    return



def parse_keyword_COMPDAT_line(well_comp_line):
    well_comp_line = re.sub('/', ' ', well_comp_line)
    well_comp_line = re.sub("'", ' ', well_comp_line)
    return well_comp_line.split()

# print(parse_keyword_COMPDAT_line("'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"))



def parse_keyword_DATE_line(current_date_line):
    current_date_line = re.sub('/', ' ', current_date_line)
    current_date_line = re.sub(r'\s+', ' ', current_date_line)
    return current_date_line
# print(parse_keyword_DATE_line("01 JUN 2018 /"))



def parse_keyword_COMDATL_line(well_comp_line):
    well_comp_line = re.sub('/', ' ', well_comp_line)
    well_comp_line = re.sub("'", ' ', well_comp_line)
    return well_comp_line.split()
# print(parse_keyword_COMDATL_line("'W3' 'LGR1' 10 10 2 2 OPEN 1* 1 2 1 3* 1.0918 /"))


def result_to_csv():
    return