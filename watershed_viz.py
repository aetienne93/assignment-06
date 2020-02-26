#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:50:45 2020
Assignment 06: graphing data with Python
@author: aetienne
@github unmane: aetienne93
This script does the following key tasks:
    1.Reads data from specified input file
    2. Processes that data 
    3. Creates graphs and charts utilizing the matplotlin library 
    4. outputs those charts to a specified PDF file    
"""

"""import all of the necessary libraries"""
import numpy as np
import matplotlib.pyplot as plt
import sys
	
"""Check for correct command line arguments"""
if len(sys.argv) != 3:
	print("Incorrect Syntax")
	print("Input: python watershed_viz.py [Source file] [Destination File]")
	sys.exit()

"""read in command line arguments to script"""
inFileName = sys.argv[1]
outFilename = sys.argv[2]

"""read in file information using genfromtxt- per tutorial given on github"""
data  = np.genfromtxt(inFileName, 
					dtype=['int','float','float','float','float','float','float'],
					names=True,
					delimiter='\t',
					autostrip=True)


"""size plot utilizing the subplot command"""
fig = plt.figure(figsize=(25,25))														
axis1 = fig.add_subplot(311)
axis2 = fig.add_subplot(312)																
axis3 = fig.add_subplot(313)																

"""create plot one- streamflow: mean, maximum, and minimum"""
axis1.plot(data['Year'],data['Mean'],'k')
axis1.plot(data['Year'],data['Max'],'r')
axis1.plot(data['Year'],data['Min'],'b')

"""create legend"""
axis1.legend(['Mean','Max','Min'])														
axis1.set_xlabel('Year')
axis1.set_ylabel('Streamflow (cfs)')
"""set xticks for yearly data assimilation"""
axis1.set_xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 12, dtype='int')])	

"""create plot two- Tqmean"""
"""create circular graph"""
axis2.plot(data['Year'],data['Tqmean']*100,'--o')											
axis2.set_xlabel('Year')
axis2.set_ylabel('Tqmean (%)')
axis2.set_xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 12, dtype='int')])	

"""create plot 3- RBindex"""
axis3.bar(data['Year'],data['RBindex'])
axis3.set_xlabel('Year')
axis3.set_ylabel('R-B Index (ratio)')
axis3.set_xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 15, dtype='int')])	

"""Save figure and output to specified file name- specify PDF in command line arg"""
plt.savefig(outFilename)