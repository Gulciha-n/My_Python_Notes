import os 

#current working directory
print(os.getcwd())

#changing a directory = chdir
os.chdir(r"the address of directory")

#list directory
print(os.listdir(r"the address of the directory you want to see"))

#list directory with for loop
for file in os.listdir():
    print(file)
    
#generating a directory
os.mkdir("directory name")

#nested directories
os.makedirs("dir1\\dir2")
print(os.listdir())

#deleting a directory
os.rmdir("directory name")

#delete nested directories
os.removedirs("dir1\\dir2\\dir3.....")

#deleting a file
os.remove(r"file path","file name")

#rename if you are in the same directory
os.rename(r"file_name.docx", "rename.docx")

#rename if you are in the different directory
os.rename(r"path", "new_name")

#statistics
os.stat(r"file path or file name")

#file size as byte
 
#showing all directories and files in a directory
for directory1 , in_directory1 , in_file in os.walk(r"path"):
    print("The directories:",directory1)
    print("in directories:",in_directory1)
    print("Files :",in_file)
    print()
    

#generating a file path
os.path.join("a", "paths")

#is it a file?  it returns True or False 
os.path.isfile(r"path")

#is it a directory?  it returns True or False 
os.path.isdir(r"path")

#showing extension of files
os.path.splitext(r"path")





