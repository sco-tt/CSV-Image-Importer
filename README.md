CSV image importer
================  

## About
This is a quick command line script for downloading files when their path is specified in a CSV file. It was written as part of a website migration project. 

Imagine a CSV export like this

Title | Author | Category | Featured Image
--- | --- | --- | ---  
My Favorite Disco Song | Scott | Music Criticism | /images/arnie-love-and-the-lovelettes.jpg
My Favorite Winter Socks | Gil | Fashion | /images/my-fav-socks.jpg

## Use
The script is used from the command line and takes three paramters
`python importer.py [file name] [column name] [base url]`

The script produces some output in the shell for each column in the CSV:
`Downloaded http://scottpinkelman.com/images/hello.jpg on Row 611 of 661
20`
`No image file found on Row 612 of 661`

Files are saved in images/csv name. E.g. if the CSV is called News.csv the files will be saved in images/news.

**Example**
`python importer.py posts.csv featured_image http://scottpinkelman.com`

##Notes
The above example assumes that the base URL slash is defined in the CSV image column. If instead the export looks like this:

Title | Author | Category | Featured Image
--- | --- | --- | ---  
My Favorite Disco Song | Scott | Music Criticism | images/arnie-love-and-the-lovelettes.jpg
My Favorite Winter Socks | Gil | Fashion | images/my-fav-socks.jpg

Then the command would need to be adjusted accordingly:
`python importer.py posts.csv featured_image http://scottpinkelman.com/`