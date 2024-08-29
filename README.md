<h1>Handy_Scripts</h1>
<p>This repository contains a collection of automation scripts, designed to help manage and organize your operating system and files. The goal is to showcase various scripts, that can streamline common tasks and keep your system organized.</p>

<h2>FolderSorter</h2>
<p>FolderSorter is a python script that helps organise messy folders. It takes all files in the current working directory, and moves them to a "sorted_folder". Then, sub-directories are created inside the "sorted_folder", based on the files that have moved. For example, if the files that have moved to "sorted_folder" are of file type txt, png and pdf. Then, three sub-directories will be created, txt, png and pdf. The files will then move to the corresponding sub-directory</p>

<ul>
	<li>hello_world.txt > txt (folder)</li>
	<li>family_photo.png > png (folder)</li>
</ul>

<h3>Usage</h3>
Unix systems
```
python3 FolderSorter.py [folder_name] [move_folder]
```

<ul>
	<li>[folder_name] (optional): Specify a custom name for the "sorted_folder". If not provided, the default name "sorted_folder" will be used.</li>
	<li>[move_folder] (optional): Set to "yes" to move all files, including directories, or "no" to move only non-directory files. If not provided, the default behavior is to move only non-directory files.</li>

</ul>

<h3>Example Usage</h3>
```
python3 FolderSorter.py "organized_files" yes
```