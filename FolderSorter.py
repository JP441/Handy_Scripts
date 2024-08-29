import os 
import sys
import shutil

class FolderSorter():
	def __init__(self):
		self.folder_name = "sorted_folder"
		self.move_folder = False
		self.all_files = os.listdir()
		self.no_dir_files = []
		self.file_types = set()
		self.RED = "\033[31m"
		self.GREEN = "\033[32m"
		self.RESET = "\033[0m"

	#Windows Powershell does not understand these colours, so remove if windows
	#OS is in use
	def remove_terminal_colours_windows(self):
		if sys.platform == "win32":
			self.RED = ""
			self.GREEN = ""
			self.RESET = ""

	def read_user_arguments(self):
		try:
			if len(sys.argv) == 2:
				self.folder_name = str(sys.argv[1])
			elif len(sys.argv) == 3:
				self.folder_name = str(sys.argv[1])
				self.check_move_folder_arg(str(sys.argv[2]).lower())
			elif len(sys.argv) > 3:
				print(
					f"{self.RED}Too many arguments inputted, can only take 2 " 
					"(folder_name and move_folder) please refer to Github " 
					"README for help"
					)
				sys.exit()
		except ValueError as ve:
			print(ve)
			sys.exit()

	def check_move_folder_arg(self, arg):
		if arg == "yes".lower():
			self.move_folder = True
		elif arg == "no".lower():
			self.move_folder = False
		else:
			raise ValueError(
				f"{self.RED} please type yes or no for arg 2 please refer to "
				"Github README for help")

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
						print(f"{self.GREEN} {x} directory created")
					else:
						os.mkdir("no_file_type")
						print(f"{self.GREEN} no_file_type directory created")
				except FileExistsError:
					pass

	def move_all_files_to_sorted(self):
		print(f"############ moving files to {self.folder_name} ############")
		if not self.move_folder:
			files = self.no_dir_files
		else:
			files = self.all_files
		if self.folder_name in files:
			files.remove(self.folder_name)
		for file in files:
			try: 
				shutil.move(file, self.folder_name)
				self.print_file_move_location(file, self.folder_name)
			except shutil.Error:
				self.print_file_collision_error(file, self.folder_name)

	def print_file_collision_error(self, file, folder_name):
		msg = (
			f"Could not move {file} to {folder_name} " 
			"as it already exists")
		print(self.RED + msg)

	def print_file_move_location(self, file, folder_name):
		print(f"{self.GREEN} {file} moved to {folder_name}")	

	def get_files_that_are_not_dir(self):
		self.no_dir_files = [x for x in self.all_files if os.path.isfile(x)]

	def move_all_files_to_sub_dir(self):
		print(
			f"{self.RESET}############ moving files to sub directories " 
			"############")
		for file in self.no_dir_files:
			try:
				if len(file.rsplit(".")) == 1:
					current_file_type = "no_file_type"
				else:
					current_file_type = file.rsplit(".")[-1].strip()
				shutil.move(file, current_file_type)
				self.print_file_move_location(file, current_file_type)
			except shutil.Error:
				self.print_file_collision_error(file, current_file_type)

	def run_program(self):
		self.remove_terminal_colours_windows()
		self.read_user_arguments()
		self.make_sorted_folder()
		self.get_files_that_are_not_dir()
		self.move_all_files_to_sorted()
		os.chdir(f"{self.folder_name}")
		self.make_sub_dirs()
		self.move_all_files_to_sub_dir()

fs = FolderSorter()
fs.run_program()
	



