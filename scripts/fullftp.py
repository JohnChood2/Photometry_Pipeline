#! /usr/bin/python

# """
# make a file of all the fits file names
# read the file and put to dummyfile
# then loop through all the elements in dummyfile
# """

from astropy.io import fits
import os, sys
import numpy as np

def Index(directory, datatype):
    """
    Indexes the files in a directory 'directory' with a specific data type.

    Parameters
    ----------
    directory: string
        Absolute path to the folder that is indexed

    datatype: string
        Data type fo the files to be indexed in the folder

    Returns
    -------
    file_array: array_like
        numpy.array of indexed files in the folder 'directory' with specific
        datatype.
    """
    assert(os.path.exists(directory))
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            if file.endswith(datatype):
                fullname = os.path.join(directory, file)
                files.append(fullname)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    stack.append(fullname)
    files = np.array(files)

    return files

def Path_Folder(directory):
    """
    Determines if folder exists. It creates it otherwise.

    Parameters
    ----------
    directory: string
        Absolute path of the expected directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

# Creating new folder
Output_dir = os.getcwd()+'/photometric_nights/output'
Path_Folder(Output_dir)
# Output file
Out_file = '{0}/full_list.txt'.format(Output_dir)
# Files in the directory
Data_Dir = os.getcwd()+'/photometric_nights/'
Path_Folder(Data_Dir)
# Get list of files in Data_Dir with 'extension'
file_ext = '.fits'
file_list = Index(Data_Dir, file_ext)
# Creating arrays
Obj_arr      = [ [] for x in xrange(len(file_list))]
fil_arr      = [ [] for x in xrange(len(file_list))]
filename_arr = [ [] for x in xrange(len(file_list))]
# Looping over all files
ii = 0
for file in file_list:
    file_data, file_header = fits.getdata(file, header=True)
    Obj_arr      [ii] = file_header['OBJECT']
    filename_arr [ii] = os.path.basename(file)
    fil_arr      [ii] = file_header['CCDFLTID']
    ii += 1

# To numpy arrays
Obj_arr      = np.array(Obj_arr)
fil_arr      = np.array(fil_arr)
filename_arr = np.array(filename_arr)
# Saving to file
np.savetxt(Out_file, np.column_stack((Obj_arr, fil_arr, filename_arr)), 
delimiter="   ", fmt=["%10s", "%10s", "%10s"]  )




