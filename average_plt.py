import tecplot as tp
import numpy as np
import os
import sys

rootDir = '../Data/CUTS'

# Loop over files in directory
for dirName, subdirList, fileList in os.walk(rootDir):
  print('Found directory: %s' % dirName)
  for filename in fileList:
    print('\t%s' % filename)

    # filename = 'xcut0.366200.plt' 
    ds = tp.data.load_tecplot(rootDir + '/' + filename)

    # Check zone type
    # print(ds.zone(0))
    # If you want to print zone values
    #x_vals = ds.zone(0).values('X')
    
    # Extract slice
    extracted_slice = tp.data.extract.extract_slice(
        origin=(-4.3694003417E-05, 0, 0),
        normal=(1, 0, 0),
        dataset=ds)
    
    #print extracted_slice
    
    # Store coordinates
    x_vals = extracted_slice.values('X')
    y_vals = extracted_slice.values('Y')
    z_vals = extracted_slice.values('Z')
    
    # Store scalars
    T_vals = extracted_slice.values('T')
    
    #print x_vals.as_numpy_array()
    
    # Range of points to average over
    x = -4.3694003417E-05
    ymin = -0.025
    ymax = 0.025
    z = -0.23
    num_points = 10
    xcoords = x*np.ones(num_points)
    zcoords = z*np.ones(num_points)
    
    # Get value over line
    ycoords = np.linspace(ymin,ymax,num_points)
    line = zip(xcoords,ycoords,zcoords)
    extracted_line = tp.data.extract.extract_line(line)
    
    # Get scalars over lines
    T_vals_line = extracted_line.values('T')
    T_vals_line_arr = T_vals_line.as_numpy_array()
    
    # Print average
    print np.average(T_vals_line_arr)
    
    # Print average temperature
    #t_sum = 0.0
    #for i in range(len(yrange)):
    #  # Get value at co-ordinate
    #  t_sum = t_sum + yrange[i]
    #print t_sum/num_points
    
    # Print average pressure


