#!/usr/bin/env
"""
TODO: Add file header comment
"""
__author__ = "Michael Feist"

import sys
import os

def getReportData(filePath):
    
    # TODO: Initialize counters
    
    # TODO: Open file and put into loop by line
    
    # TODO: Loop by char
    
    # TODO: Check if char is letter/figure/other character
    
    # TODO: Add logic for checking word count
    
    # TODO: Return dictionary of each count
    pass

def writeAttributeCount(attributeName, count, file):
    pass

def writeReport(reportData):
    
    # TODO: Open file
    
    # TODO: Write lines
    pass

if __name__ == "__main__":
    # TODO: Check for no arguments given
    try:
        reportData = getReportData(sys.argv[0])
        print(reportData)
    except:
        # TODO: Handle file exceptions
        pass
    
    try:
        writeReport(reportData)
    except:
        # TODO: Handle file exceptions
        pass
