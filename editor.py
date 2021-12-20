from os import error
from time import time
from editors import Editor
"----- Now let's begin with the edits ----"
options = ["[1] First letter of the email is UPPER","[2] First letter of the email is LOWER","Type your option: "]
def Save(output, path=None): t = time();path = "output.txt" if path is None  else path;open(path, 'a+', encoding='utf-8').write(output);return time()-t
def inp(_type):
    if type(_type) == int: return int(input())
    elif type(_type) == str: return input()
    else: ...
def DragDrop(): x = input('Drag and drop your file: '); return x.replace('"', '') if x.startswith('"') and x.endswith('"') else x
def Menu():
    [print(each) for each in options]; option = inp(0); drop = DragDrop(); file = open(drop, 'r', encoding='utf-8', errors='ignore').readlines()
    if '' in file: file.remove('')
    if option == 1: t = time();z = Editor.BigStartswithEmail(map(str, file));print(f'Edited in {time() - t}');t = "".join(each for each in z);output = Save(t ,'output.txt');print('Saved in ', output)
    elif option == 2: t = time(); z = Editor.SmallStartswithEmail(map(str, file)); print(f'Edited in {time() - t}'); t = "".join(each for each in z); output = Save(t ,'output.txt'); print('Saved in ', output)
Menu()