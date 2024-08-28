import os 
import sys
import shutil

class FolderSorter():
	def __init__(self):
		self.folder_name = "sorted_folder"
		self.move_folder = True
		self.all_files = os.listdir()
		print(self.all_files)
		self.no_dir_files = []
		self.file_types = set()
		self.RED = "\033[31m"

	def make_sorted_folder(self):
		try:
			os.mkdir(self.folder_name)
		except FileExistsError:
			pass
		except FileNotFoundError:
			print(f"") #TO add
			sys.exit()

	def make_sub_dirs(self):
			for x in self.no_dir_files:
				self.file_types.add(os.path.splitext(x)[1].strip(".").strip())
			for x in self.file_types:
				try:
					if x != '':
						os.mkdir(x)
					else:
						os.mkdir("no_file_type")
				except FileExistsError:
					pass

	def move_all_files_to_sorted(self):
		if not self.move_folder:
			files = self.no_dir_files
		else:
			files = self.all_files
		for file in files:
			try: 
				shutil.move(file, self.folder_name)
			except shutil.Error:
				self.print_file_collision_error(file, self.folder_name)

	def print_file_collision_error(self, file, folder_name):
		msg = (
			f"Could not move {file} to {folder_name} " 
			"as it already exists")
		print(self.RED + msg)

	def get_files_that_are_not_dir(self):
		self.no_dir_files = [x for x in self.all_files if os.path.isfile(x)]

	def move_all_files_to_sub_dir(self):
		for file in self.no_dir_files:
			try:
				if len(file.rsplit(".")) == 1:
					current_file_type = "no_file_type"
				else:
					current_file_type = file.rsplit(".")[-1].strip()
				shutil.move(file, current_file_type)
			except shutil.Error:
				self.print_file_collision_error(file, current_file_type)

	def run_program(self):
		self.make_sorted_folder()
		self.get_files_that_are_not_dir()
		self.move_all_files_to_sorted()
		os.chdir(f"{self.folder_name}")
		self.make_sub_dirs()
		self.move_all_files_to_sub_dir()

fs = FolderSorter()
fs.run_program()
	



