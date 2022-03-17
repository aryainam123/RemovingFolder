import os
import shutil
import time

def main():
	deletedFoldersCount = 0
	deletedFilesCount = 0
	path = input("Enter the path")
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)
	if os.path.exists(path):
		for rootFolder, folders, files in os.walk(path):
			if seconds >= getFileOrFolderAge(rootFolder):
				removeFolder(rootFolder)
				deletedFoldersCount += 1
				break

			else:
				for folder in folders:
					folder_path = os.path.join(rootFolder, folder)
					if seconds >= getFileOrFolderAge(folder_path):
						removeFolder(folder_path)
						deletedFoldersCount += 1
				for file in files:
					file_path = os.path.join(rootFolder, file)
					if seconds >= getFileOrFolderAge(file_path):
						removeFile(file_path)
						deletedFilesCount += 1
		else:
			if seconds >= getFileOrFolderAge(path):
				removeFile(path)
				deletedFilesCount += 1

	print(f"Total folders deleted: {deletedFoldersCount}")
	print(f"Total files deleted: {deletedFilesCount}")


def removeFolder(path):
	if not shutil.rmtree(path):
		print("Folder removed")

def removeFile(path):
	if not os.remove(path):
		print("File removed")

def getFileOrFolderAge(path):
	ctime = os.stat(path).st_ctime
	return ctime

if __name__ == '__main__':
	main()
	
	
	
