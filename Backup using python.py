import os
import shutil

source= input("Enter source file name ")
destination= input ("Enter destination for backup ")

source= source+'/'
destination= destination+'/'

listofiles=os.listdir(source)
for file in listofiles:
    shutil.move((source+file), destination)