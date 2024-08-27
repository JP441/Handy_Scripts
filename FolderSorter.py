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
			for file in self.no_dir_files:
				try:
					shutil.move(file, self.folder_name)
				except shutil.Error: 
					print(f"Could not move {file} to {self.folder_name} "
					 "as it already exists")
			return
		for file in self.all_files:
			try:
				shutil.move(file, self.folder_name)
			except shutil.Error: 
				print(f"Could not move {file} to {self.folder_name} "
				 "as it already exists")

	def get_files_that_are_not_dir(self):
		self.no_dir_files = [x for x in self.all_files if os.path.isfile(x)]

	def move_all_files_to_sub_dir(self):
		for file in self.no_dir_files:
			if len(file.rsplit(".")) == 1:
				current_file_type = "no_file_type"
			else:
				current_file_type = file.rsplit(".")[-1].strip()
			shutil.move(file, current_file_type)

	def run_program(self):
		self.make_sorted_folder()
		self.get_files_that_are_not_dir()
		self.move_all_files_to_sorted()
		os.chdir(f"{self.folder_name}")
		self.make_sub_dirs()
		self.move_all_files_to_sub_dir()

fs = FolderSorter()
fs.run_program()
	



