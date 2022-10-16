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

import sys
import os
import datetime

def isAlpha(char):
    return char.isalpha()

def isWordSeparator(char):
    asciiValue = ord(char)
    if asciiValue == ord('\t') or asciiValue == ord('\n') \
        or asciiValue == ord(' ') or asciiValue == ord('\r'):
        return True
    else:
        return False

def isIgnoredChar(char):
    asciiValue = ord(char)
    if (asciiValue >= 0 and asciiValue <= 32) or (asciiValue == 127):
        return True
    else:
        return False

def isFigure(char):
    asciiValue = ord(char)
    if (asciiValue >= ord('!') and asciiValue <= ord('/')) or (asciiValue >= ord(':') and asciiValue <= ord('@')) \
        or (asciiValue >= ord('[') and asciiValue <= ord('`')) or (asciiValue >= ord('{') and asciiValue <= ord('~')):
            return True
    else:
        return False
    
def updateWordsOfSize(numWordsOfSize, wordSize):
    try:
        numWordsOfSize[wordSize] = numWordsOfSize[wordSize] + 1
    except:
        numWordsOfSize[wordSize] = 0

def getReportData(filePath):
    fileName = os.path.normpath(filePath)
    numLines = 0
    numChars = 0
    numLetters = 0
    numFigures = 0
    numOtherCharacters = 0
    numWords = 0
    numWordsOfSize = dict()
    
    with open(filePath, 'r') as f:
        for line in f:
            
            numLines += 1
            currentWordSize = 0
            inWord = False
            
            for char in line:
                
                shouldCountChar = not isIgnoredChar(char)
                
                if isAlpha(char):
                    numLetters += 1
                    currentWordSize += 1
                    inWord = True
                elif isFigure(char):
                    numFigures += 1
                elif shouldCountChar:
                    numOtherCharacters += 1
                    
                if shouldCountChar:
                    numChars += 1
                    
                if inWord and isWordSeparator(char):
                    numWords += 1
                    updateWordsOfSize(numWordsOfSize, currentWordSize)
                    currentWordSize = 0
                    inWord = False
    
    return {"File Name" : fileName, "Line Count" : numLines, "Char Count" : numChars, \
        "Letter Count" : numLetters, "Figure Count" : numFigures, \
        "Other Char Count" : numOtherCharacters, "Word Count" : numWords, \
        "Words of Size" : numWordsOfSize}

def writeAttributeCount(attributeName, count, file):
    file.write(f'Number of {attributeName}: {count}')

def writeReport(reportData):
    currentDate = datetime.datetime.now()
    
    reportFileName = f'.\Reports\{os.path.basename(reportData["File Name"])}_\
        report_{currentDate.month}_{currentDate.day}_{currentDate.year}'
    
    with open(reportFileName, 'w') as f:
        f.write(f'File name: {os.path.abspath(reportData["File Name"])}\n')
        writeAttributeCount('lines', reportData["Line Count"], f)
        writeAttributeCount('characters (total)', reportData["Char Count"], f)
        writeAttributeCount('letters', reportData["Letter Count"], f)
        writeAttributeCount('figures', reportData["Figure Count"], f)
        writeAttributeCount('other characters', reportData["Other Char Count"], f)
        writeAttributeCount('words', reportData["Word Count"], f)
        for wordSize in reportData["Words of Size"]:
            writeAttributeCount(f'{wordSize} letter words', reportData["Words of Size"][wordSize], f)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print('FileReporter must have one and only one argument')
        exit(1)
        
    try:
        reportData = getReportData(sys.argv[0])
        print(reportData)
    except:
        print('Problem opening read file\n')
        exit(1)
    
    try:
        writeReport(reportData)
    except:
        print('Problem opening write file\n')
        exit(1)
