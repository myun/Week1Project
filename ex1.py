import string
import os
import shutil

alphabet = string.lowercase
alphabet = list(alphabet)

#os.mkdir("test")

[os.mkdir(letter) for letter in alphabet]
    

#shutil.move("original_files/aexwin.txt", "a")

for fn in os.listdir("original_files"):
    first_letter = fn[0]
    #print os.getcwd()
    sourcefile =  "original_files/"+fn
    shutil.move(sourcefile, first_letter)