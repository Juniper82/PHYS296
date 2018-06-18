# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 18:33:00 2018

@author: Tiffany
"""
from __future__ import print_function
import os

os.chdir("C:\\Users\\Aardvark\\Documents\\Py\\phys_summer")
path = "C:\\Users\\Aardvark\\Documents\\GIT\\fitpack"
# path = "C:\\Users\\Tiffany\\Documents\\Py\\phys_summer\\folder"

file_directry_list = []
for root, dirs, files in os.walk(path):
    for file in files:
        file_directry_list.append(os.path.join(root, file))


def check_file(dependence, file_directry_list):
    if "." in dependence:
        folder_dependence = dependence.split(".")[-2]
        dependence = dependence.split(".")[-1]
    else:
        folder_dependence = None
    for path in file_directry_list:
        if dependence in path.split("\\")[-1] and dependence != "os":
            if folder_dependence is None:
                return (dependence + ";" + path[27:])
            elif folder_dependence in path.split("\\")[-2]:
                return (folder_dependence + "." + dependence + ";" + path[27:])
    return (dependence + "; outside_fitpack")


def annotate(parent_file, target_dependence):
    with open("fitpack_structure.txt", "a") as notepad:
        notepad.write("parent_file\n")
        notepad.write("   " + parent_file[27:] + "\n")
        for dependence in target_dependence:
            notepad.write("    -" + check_file(dependence, file_directry_list)
                          + "\n")


for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".py"):
            parent_file = os.path.join(root, file)
            target_dependence = []
            for line in open(parent_file):
                if "from" in line.split():
                    marks = line.split()[1]
                    if "," in marks:
                        for x in marks.split(","):
                            target_dependence.append(x)
                    else:
                        target_dependence.append(marks)
#                    print("from")
#                    print(target_dependence)
                elif "import" in line.split() and "from" not in line.split():
                    marks = line.split()[1]
                    if "," in marks:
                        for x in marks.split(","):
                            target_dependence.append(x)
                    else:
                        target_dependence.append(marks)
            annotate(parent_file, target_dependence)
