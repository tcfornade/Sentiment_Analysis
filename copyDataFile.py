import os
import shutil

def copy_data_file(filenameIN, filenameOUT):
    if os.path.isfile(filenameIN):
        try:
            shutil.copyfile(filenameIN, filenameOUT)
            print(f"File '{filenameIN}' copied to '{filenameOUT}' successfully.")
        except Exception as e:
            print(f"An error occured while copying the file: {e}")
    else:
        print(f"File '{filenameIN}' does not exist.")
 