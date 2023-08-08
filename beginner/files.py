#import os
#path = "C:\\Users\\nagen\\Desktop"
#if os.path.exists(path):
 #   print("That location is exists")
 #   if os.path.isfile(path):
 #       print("That is a file")
 #   elif os.path.isdir(path):
 #       print("That is a directory")
#else:
#    print("that location doesn't exists")

#read file :

#with open('variables.py') as file:
#    print(file.read())

#print(file.closed)

#with open('loop.p') as file:
#    print(file.read())

#try:
#    with open('loop.py') as file:
#        print(file.read())
#except FileNotFoundError:
#    print("The file was not found")


# write a file :
#text = "ohoooooo\nThere is some text here\nit's interesting\n"
#text = "have a nice day"
#with open('text.txt','w') as file:
#with open('text.txt','a') as file:
#    file.write(text)

#copy file :
#copyfile() = copies contents of a file
#copy() = copyfile()  + permission mode + destination can be a directory
#copy2() = copy() + copies metadata(file's creation and modification times)

#import shutil

#shutil.copyfile('text.txt', 'copy.txt')      #src.dst
#shutil.copyfile('text.txt','C:\\Users\\nagen\\Desktop\\copy.txt' )
#shutil.copy2('text.txt','C:\\Users\\nagen\\Desktop\\copy.txt')

# move a file :
#import os

#source = "folder"
#destination = "C:\\Users\\nagen\\Desktop\\folder"

#try:
#    if os.path.exists(destination):
#        print("There is already a file there")
#    else:
#        os.replace(source,destination)
#        print(source+"was moved")
#except FileNotFoundError:
#  print(source+"was not found")

#delete a file
import os
import shutil
#path = "test.txt"
#path = "empty_folder"
path = "folder"
try:
    #os.remove(path)            #delete a file
    #os.rmdir(path)             #for empty folder
     shutil.rmtree(path)        #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot deleted that using that function")
else:
    print(path+"was deleted")
#os.remove(path)
#os.remove('test.txt')