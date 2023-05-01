import main
import parser1
from urllib.parse import urlparse
import os
import pandas as pd


def pass_info():
	value = ''
	w_timetable = main.get_list_files_timetables()[0]
	w_timetable = urlparse(w_timetable)
	w_timetable= os.path.basename(w_timetable.path)

	w_swaps_file_name     = main.get_list_files_swap()[-1]
	print('==== ',w_timetable)
	print('==== ',w_swaps_file_name)

	w_swaps = urlparse(w_swaps_file_name)
	w_swaps = os.path.basename(w_swaps.path)


	w_timetable_time = main.get_time_time()
	w_swaps_time     = main.get_time_swap()

	return w_timetable, w_swaps_file_name, w_swaps, w_timetable_time, w_swaps_time

def get_surnames(w_swaps_file_name):
	teachers_list = parser1.get_names_list(w_swaps_file_name)
	teachers_list = [x.split(' ')[0] for i, x in enumerate(teachers_list)]
	teachers_list = pd.unique(teachers_list).tolist()

	return teachers_list, len(teachers_list)

def get_surnames_with_otch(w_swaps_file_name):
	teachers_list = parser1.get_names_list(w_swaps_file_name)
	teachers_list = pd.unique(teachers_list).tolist()
	teachers_list_otch = [x.split(' ')[0] for i, x in enumerate(teachers_list)]
	teachers_list_otch = pd.unique(teachers_list_otch).tolist()

	return teachers_list, teachers_list_otch, len(teachers_list)
