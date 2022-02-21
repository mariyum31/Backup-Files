import os
import time
import shutil

def main():
    deleted_folders_count = 0
    deleted_files_count = 0

    path = "/Path_to_Delete"
    days = 30
    
    seconds = time.time()
    
    if os.path.exists(path):
        
        for root_folder, folders, files in os.walk(path):
            if seconds >= getFileOrFolderAge(root_folder):
                removeFolder(root_folder)
                deleted_folders_count += 1

                break

            else:
                for folder in folders:
                    folderPath = os.path.join(root_folder, folder)

                    if seconds >= getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deleted_folders_count += 1
                
                for file in files:
                    filePath = os.path.join(root_folder, file)

                    if seconds >= getFileOrFolderAge(filePath):
                        removeFile(filePath)
                        deleted_files_count += 1
        
        else:
            if seconds >= getFileOrFolderAge(path):
                removeFile(path)
                deleted_files_count += 1
    
    else:
        print('"{path}" is not found!')
        deleted_files_count += 1 
    
    print("Total folders deleted: {deleted_folders_count}")
    print("Total files deleted: {deleted_files_count}")

def removeFolder(path):
    
    if not shutil.rmtree(path):
        print("{path} is removed successfully")

	else:
        print("Unable to delete the "+path )

def removeFile(path):
    
    if not os.remove(path):
        print("{path} is removed successfully")
    
    else:
        print("Unable to delete the "+path )

def getFileOrFolderAge(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime

if __name__ == '__main__':
	main()
