import os
import string

def rename_files():

  #(1) get file names from a folder
  file_list = os.listdir("/full-path-goes-here/python-bits/rename_these_files")

  saved_path = os.getcwd()
  os.chdir("/full-path-goes-here/python-bits/rename_these_files")

  #(2) for each file, rename file
  for file_name in file_list:
    new_name = file_name.translate(None, "0123456789")
    print("Old Name - " + file_name + " New Name - " + new_name)
    os.rename(file_name, new_name)

  os.chdir(saved_path)

rename_files()