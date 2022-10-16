import unittest
import FileReporter
import filecmp
import os

class TestFileReporter(unittest.TestCase):
    testInDirectory = 'TestDataFiles\In\\'
    testOutDirectory = 'TestDataFiles\Out\\'
    
    def test_updateWordsOfSize(self):
        expectedCount = 1
        testWordSize = 3
        
        testDict = dict()
        FileReporter.updateWordsOfSize(testDict, testWordSize)
        
        self.assertEqual(expectedCount, testDict[testWordSize])
        
        expectedCount = 2
        
        FileReporter.updateWordsOfSize(testDict, testWordSize)
        
        self.assertEqual(expectedCount, testDict[testWordSize])
        
    def runTestGetReportData(self, fileName, lineCount, charCount, letterCount, figureCount, otherCharCount, wordCount, wordsOfSizeLength):
        testReportData = FileReporter.getReportData(fileName)
        self.assertEqual(testReportData["File Name"], fileName)
        self.assertEqual(testReportData["Line Count"], lineCount)
        self.assertEqual(testReportData["Char Count"], charCount)
        self.assertEqual(testReportData["Letter Count"], letterCount)
        self.assertEqual(testReportData["Figure Count"], figureCount)
        self.assertEqual(testReportData["Other Char Count"], otherCharCount)
        self.assertEqual(testReportData["Word Count"], wordCount)
        self.assertEqual(len(testReportData["Words of Size"].items()), wordsOfSizeLength)
    
    def test_getReportData(self):
        
        self.runTestGetReportData(
            fileName=f'{self.testInDirectory}test_0.in',
            lineCount=3,
            charCount=32,
            letterCount=26,
            figureCount=0,
            otherCharCount=6,
            wordCount=7,
            wordsOfSizeLength=5
            )
        
        self.runTestGetReportData(
            fileName=f'{self.testInDirectory}test_1.in',
            lineCount=0,
            charCount=0,
            letterCount=0,
            figureCount=0,
            otherCharCount=0,
            wordCount=0,
            wordsOfSizeLength=0
            )
        
        self.runTestGetReportData(
            fileName=f'{self.testInDirectory}test_2.in',
            lineCount=1,
            charCount=26,
            letterCount=14,
            figureCount=10,
            otherCharCount=2,
            wordCount=3,
            wordsOfSizeLength=3
            )
    
    def runTestWriteReport(self, testFile):
        testReportData = FileReporter.getReportData(f'{self.testInDirectory}{testFile}.in')
        FileReporter.writeReport(testReportData)
        self.assertTrue(filecmp.cmp(f'{FileReporter.generateReportFilename(testReportData)}', \
            f'{self.testOutDirectory}{testFile}.out'))
        os.remove(FileReporter.generateReportFilename(testReportData))
    
    def test_writeReport(self):
        self.runTestWriteReport('test_0')
        
        self.runTestWriteReport('test_1')
        
        self.runTestWriteReport('test_2')
    
if __name__ == '__main__':
    unittest.main()