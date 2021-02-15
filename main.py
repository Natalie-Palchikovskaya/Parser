#-*- coding: utf-8 -*-
from lib import schedule_parser


#def... вспомогательные функции
if __name__ == "__main__":
    #при импорте не будет ниже реализовываться
    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters = ()
    input_file = "input_data/test_shedule.inc"
    output_csv = "output_data/schedule/csv"


    schedule_df = schedule_parser.transform(keywords,parameters,
                                           input_file, output_csv)

print(input_file)