#! /usr/bin/env python

import matplotlib
matplotlib.use( 'Agg' )

import sys
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

### From http://docs.astropy.org/en/stable/io/fits/
### Under "Working With Table Data"
###
### Defining Filename ###

Args_array      = np.array( sys.argv )
File_N  = Args_array[1]

# File_N = '3C454.3_604800.lc'
# Reading File #

hdulist = fits.open(File_N)

# Reading Data

tbdata = hdulist[1].data

## Available variables in the file ##

Var_Names = tbdata.names
print Var_Names

## Using Data ##

X_axis_variable     = 'START'
Y_axis_variable     = 'FLUX_300_1000'
Y_axis_variable_err = 'ERROR_300_1000'
Plot_color          = 'r'

X_arr               = tbdata[ X_axis_variable     ]
Y_arr               = tbdata[ Y_axis_variable     ]
Y_err_arr           = tbdata[ Y_axis_variable_err ]

## Filtering out data ##
if Y_axis_variable == 'FLUX_300_1000':
	Y_arr_idx = np.where( Y_arr >= 0)[0]
	X_arr     = X_arr    [Y_arr_idx]
	Y_arr     = Y_arr    [Y_arr_idx]
	Y_err_arr = Y_err_arr[Y_arr_idx]

## Plotting routine ##
plt.clf() ## Clears previous figures ##
plt.close()
fig = plt.figure()
ax = fig.add_subplot( 111, axisbg='white')
ax.set_xlabel('START', fontsize=18)
ax.set_ylabel('FLUX', fontsize=18)
ax.set_title( '{0} vs {1}'.format(X_axis_variable, Y_axis_variable), fontsize=20)
ax.errorbar(X_arr, Y_arr, yerr=Y_err_arr, 
    color=Plot_color, markersize=5, fmt = 'o', linewidth=3, 
    ecolor=Plot_color, elinewidth=2, capthick = 3 
    )#, label=r'\boldmath $\overline{\mathrm{Cens}}$' )
ax.set_yscale('log')
plt.tight_layout()
fname = 'Plot_{0}_{1}.png'.format(X_axis_variable, Y_axis_variable)
plt.savefig( fname, bbox_inches='tight' )
print( '    Figure: {0}'.format( fname ))
plt.clf()
plt.close()
