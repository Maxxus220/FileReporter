# FileReporter
Program that takes one command line argument, a file path, then opens that file
and creates a report of the form:

File name: D:\temp\file.txt
Number of lines: 85
Number of characters (total): 1441
Number of letters: 782
Number of figures: 17
Number of other characters: 642
Number of words: 195
Number of 1 letter words: 56
Number of 2 letter words: 27
[...]
Number of 16 letter words: 2
Number of 19 letter words: 1

under the name file.txt_report_mm_dd_yyyy.txt inside of the Reports folder

## How to Use
Run python FileReporter.py with one argument (a file path to the file you would like to create a report on)
The corresponding report will be placed inside the reports folder

To run, the local directory of FileReporter.py must contain a folder named Reports

## Tests
Tests are contained within the TestFileReporter.py file and use unittest
To run tests simply run python TestFileReporter.py
Sample input files are contained within ./TestDataFiles/In/
Sample output files are contained within ./TestDataFiles/Out/
Note: Tests automatically remove any reports they created