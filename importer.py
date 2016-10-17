import csv
import os
import urllib
import sys

def csvImporter():
  
  # The name of the file (Posts.csv) will become the path for our download directory
  destPathName = 'images/' + sys.argv[1].lower().replace('.csv', '');

  if not os.path.isdir(destPathName):
    os.makedirs(destPathName)

  with open(sys.argv[1], 'rb') as File:
    reader = csv.DictReader(File)
    # Get the the length of rows in our CSV so we can iterate through each one
    rows = list(reader)
    totalrows = len(rows)
    totalSaved = 0;
    
    for i, row in enumerate(rows):
      if row[sys.argv[2]]:
        sourcePathName = row[sys.argv[2]]
        # Source URL to downlad from
        fileURL = sys.argv[3] + sourcePathName;
        # Cleanup the file name
        fileName = sourcePathName.replace('/', '-')[1:]
        # Save locally and print a message
        fullfilename = os.path.join(destPathName, fileName)
        urllib.urlretrieve(fileURL, fullfilename);
        print("Downloaded %s on row %d of %d" % (fileURL, i+1, totalrows))
        totalSaved += 1
        print totalSaved
      else:
        print("No image file found on row %d of %d" % (i+1, totalrows))

  print("Saved a total of %d images out of %d total rows in the file %s" % (totalSaved, totalrows, sys.argv[1]))

# Run from the command line
if __name__ == "__main__":
    csvImporter()