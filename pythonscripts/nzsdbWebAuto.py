# Easiest to run on in an Anaconda environment. The Specdal module must be added.
import specdal
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Python variables that adopt field values from the 'Plant Sample Form' in the database. #form value name
Date = "20200528"     #Collection Date. Currently ddMMyy, perhaps best if yyMMdd
Location = "UU"     #Collection Site Prefix
wd = r"C:\Users\Ellis\Desktop\spectest"   #Uploaded Spectral Images directory (Azure file services, dropbox, etc)


# This section renames the .asd files uploaded via the form submission to the work directory.
def main():
   i = 0

   for filename in os.listdir(wd):
      fileindex = filename[-8:]
      my_dest =str(Date) + "_" + str(Location) + "_" + fileindex    #suggestions: swap loc and date, or add taxon info
      my_source =wd + "\\" + filename
      my_dest =wd + "\\" + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
#Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()


# This section reads the .asd files asd files uploaded via the form submission to the work directory.
# It can output both a graph (.png) of the spectral readings, and/or a its tabled values (exportable to csv).

wd2 = r"C:\Users\Ellis\Desktop\spectest\20200528_UU_0081.asd"
# Reads a single spectrum file (wavelength/reflectance measurement)
leaf = specdal.spectrum.Spectrum(name=str('leaf_reflect'), filepath=wd2)
leaf.measurement.plot()    # database suitable plot
print(leaf)             #view spectrum value data.

# Creates a 'collection' that can contain multiple read spectrum values and their data.
plants = specdal.collection.Collection(name=str('plant_coll'))
plants.append(leaf)     # adds specdal spectrum value to the collection.

# The most effective method to use this module would be to create a collection, and then iterate through the 
# working directory for a spectral plant form, reading and appending each spectrum.
# Once collated, use the data to output the desired figures 
# (a plot of each asd, a plot of the mean values of each spectrum, or a spreadsheet).
drct = r"C:\Users\Ellis\Desktop\spectest"
plantAsds = specdal.collection.Collection(name=str('plant_coll'))
for asd in os.listdir(drct):
    asdRead = specdal.spectrum.Spectrum(asd)
    plantAsds.append(asdRead)
