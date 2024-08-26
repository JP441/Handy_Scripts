import os 
import sys

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

def make_sub_dirs():
	files = os.listdir()
	print(files)
	file_types = set()
	no_dir_files = [] #files that are not directories
	for x in files:
		if os.path.isfile(x):
			file_types.add(os.path.splitext(x)[1].strip(".").strip())
			no_dir_files.append(x)
	print(no_dir_files)
	for x in file_types:
		if x != '':
			os.mkdir(x)
		else:
			os.mkdir("no_file_type")
	return no_dir_files, file_types

def move_all_files_to_sorted(folder_name):
	os.system(f"mv * {folder_name}")

def move_all_files_to_sub_dir(files, file_types):
	for file in files:
		current_file_type = file.rsplit(".")[1] #problem here
		print(current_file_type)
		if current_file_type != '':
			os.system(f"mv {file} {current_file_type}")
		else:
			os.system(f"mv {file} no_file_type")






folder_name = make_sorted_folder()
move_all_files_to_sorted(folder_name)
os.chdir(f"{folder_name}")
files, file_types = make_sub_dirs()
move_all_files_to_sub_dir(files, file_types)

