import string
import shutil

alphabet = string.lowercase
alphabet = list(alphabet)


[shutil.rmtree(letter) for letter in alphabet]