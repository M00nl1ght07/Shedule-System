from scripts import script_1, script_2, script_3, script_4, script_5
import parser1 as swap_teachers
import parser2 as timetable_teachers

from glob import glob
import time, sys, os

from pathlib import Path
from config import PATH, OUTPUT_FOLDER, STATIC_EX, ALLOWED_EXTENSIONS
from dateutil.parser import parse


def get_all_teachers_name():
    arr = get_name()
    return arr

def listing_dir_by_m_time(search_dir):
    list_of_files = filter(os.path.isfile, glob(search_dir + '*') )
    list_of_files = sorted(list_of_files, key = os.path.getctime)
    print('-----------')
    print(list_of_files)
    print(list_of_files[-1])
    return list_of_files


def get_list_files_timetables():
    arr = listing_dir_by_m_time(PATH+'/upload/timetable/')
    print(PATH+'/upload/timetable/')
    print(arr)
    return arr

def get_list_files_swap():
    arr = listing_dir_by_m_time(PATH+'/upload/swaps/')
    res = []
    for i in arr:
        if i.split('.')[-1] in ALLOWED_EXTENSIONS:
            res.append(i)
    print(res)
    return res

def get_time_time():
    file_time = parse(time.ctime(os.path.getmtime(get_list_files_timetables()[-1])))
    return file_time.strftime("%d-%m-%Y, %H:%M")

def get_time_swap():
    print(get_list_files_swap())
    file_time = parse(time.ctime(os.path.getmtime(get_list_files_swap()[-1])))
    return file_time.strftime("%d-%m-%Y, %H:%M")


def api(timetable=get_list_files_timetables()[0], key_word='incognito'):
    os.makedirs(f'{PATH}/{OUTPUT_FOLDER}/{key_word}', exist_ok=True)

    dest_file = f'{PATH}/{OUTPUT_FOLDER}/{key_word}/{key_word}.xlsx'

    #excel_table = script_1(file_name=excel_table)

    script_2(src=STATIC_EX, dst=dest_file)

    script_3(file_name=timetable, key_word=key_word, output_table=dest_file)

    script_4(document_name=get_list_files_swap()[0], key_word=key_word, excel_table_name=dest_file)

    script_5(excel_table_name=dest_file)

    return dest_file    
