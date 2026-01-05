'''
    Script to compute mass densities from WRF outputs
'''

# Standard packages
from sys import argv
import numpy as np
from netCDF4 import Dataset as ncopen
import pickle as pkl


# List of variables to read from WRF file
raw_vname_list = ['QVAPOR','T','T00', 'P','PB','PH','PHB','XLAT','XLONG']

# Read WRF filename from command line
wrf_fname = argv[1]

# Name of output pickle file
output_fname = argv[2]


# Open wrf file
wrffile = ncopen( wrf_fname, 'r' )

# Load necessary variables from wrf file
raw_data_dict = {}
for vname in raw_vname_list:
    raw_data_dict[vname] = wrffile.variables[vname][0]

# Close wrf file
wrffile.close()


# Compute basic thermodynamic quantities
raw_data_dict['pressure'] = raw_data_dict['P'] + raw_data_dict['PB']
raw_data_dict['geopotential height'] = (raw_data_dict['PH'] + raw_data_dict['PHB'])/9.81
raw_data_dict['potential temperature'] = raw_data_dict['T'] + raw_data_dict['T00'] 
raw_data_dict['temperature'] = raw_data_dict['potential temperature'] * ( raw_data_dict['pressure'] / 1e5 ) ** 0.286
raw_data_dict['virtual temperature'] = raw_data_dict['temperature'] * (1+0.61*raw_data_dict['QVAPOR'] )

# Compute air density
output_dict = {}
output_dict['air density (kg/m3)'] = raw_data_dict['pressure'] / (287 * raw_data_dict['virtual temperature']  )



# Compute water vapor density
output_dict['water vapor density (kg/m3)'] = output_dict['air density (kg/m3)'] * raw_data_dict['QVAPOR']

# Compute dry air density
output_dict['dry density (kg/m3)'] = output_dict['air density (kg/m3)'] - output_dict['water vapor density (kg/m3)']

# Append some coordiante variables
output_dict['pressure (Pa)'] = raw_data_dict['pressure']
output_dict['geopotential height (m)'] = raw_data_dict['geopotential height']
output_dict['longitude (deg E)'] = raw_data_dict['XLONG']
output_dict['latitude (deg N)'] = raw_data_dict['XLAT']

# Save data as pickle file
with open( output_fname, 'wb' ) as handle:
    pkl.dump( output_dict, handle )
