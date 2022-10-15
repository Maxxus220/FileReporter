#!/usr/bin/env
"""
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
Number of 2 letters words: 27
[...]
Number of 16 letters words: 2
Number of 19 letters words: 1

under the name TODO.txt inside of the Reports folder
"""
__author__ = "Michael Feist"

from curses.ascii import isalpha
import sys
import os

def updateWordsOfSize(numWordsOfSize, wordSize):
    try:
        numWordsOfSize[wordSize] = numWordsOfSize[wordSize] + 1
    except:
        numWordsOfSize[wordSize] = 0

def iswordseparator(char):
    asciiValue = ord(char)
    if asciiValue == ord('\t') or asciiValue == ord('\n') \
        or asciiValue == ord(' ') or asciiValue == ord('\r'):
        return True
    else:
        return False

def isignoredchar(char):
    asciiValue = ord(char)
    if (asciiValue >= 0 and asciiValue <= 32) or (asciiValue == 127):
        return True
    else:
        return False

def isfigure(char):
    asciiValue = ord(char)
    if (asciiValue >= ord('!') and asciiValue <= ord('/')) or (asciiValue >= ord(':') and asciiValue <= ord('@')) \
        or (asciiValue >= ord('[') and asciiValue <= ord('`')) or (asciiValue >= ord('{') and asciiValue <= ord('~')):
            return True
    else:
        return False

def getReportData(filePath):
    numLines = 0
    numChars = 0
    numLetters = 0
    numFigures = 0
    numOtherCharacters = 0
    numWords = 0
    numWordsOfSize = dict()
    
    with open(filePath, 'r') as f:
        for line in f:
            
            currentWordSize = 0
            inWord = False
            
            for char in line:
                
                dontCountChar = isignoredchar(char)
                
                if isalpha(char):
                    numLetters += 1
                    currentWordSize += 1
                    inWord = True
                elif isfigure(char):
                    numFigures += 1
                elif not dontCountChar:
                    numOtherCharacters += 1
                    
                if not dontCountChar:
                    numChars += 1
                    
                if inWord and iswordseparator(char):
                    numWords += 1
                    updateWordsOfSize(numWordsOfSize, currentWordSize)
                    currentWordSize = 0
                    inWord = False
                    
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
