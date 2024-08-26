import os 
import sys
import shutil

def make_sorted_folder(folder_name="sorted_folder"):
	try:
		os.mkdir(folder_name)
		return folder_name
	except os.FileExistError:
		print(f"directory named {folder_name} already exists")
		sys.exit()
	except os.FileNotFoundError:
		print(f"") #TO add
		sys.exit()

def make_sub_dirs(files):
	file_types = set()
	no_dir_files = [] #files that are not directories
	for x in files:
		if os.path.isfile(x):
			file_types.add(os.path.splitext(x)[1].strip(".").strip())
			no_dir_files.append(x)
	for x in file_types:
		if x != '':
			os.mkdir(x)
		else:
			os.mkdir("no_file_type")
	return no_dir_files, file_types

def move_all_files_to_sorted(folder_name):
	files = os.listdir()
	for file in files:
		if os.path.isfile(file):
			shutil.move(file, folder_name)
	return files


def move_all_files_to_sub_dir(files, file_types):
	print(files)
	for file in files:
		if len(file.rsplit(".")) == 1:
			current_file_type = "no_file_type"
		else:
			current_file_type = file.rsplit(".")[-1].strip()
		shutil.move(file, current_file_type)






folder_name = make_sorted_folder()
files = move_all_files_to_sorted(folder_name)
os.chdir(f"{folder_name}")
files, file_types = make_sub_dirs(files)
move_all_files_to_sub_dir(files, file_types)

