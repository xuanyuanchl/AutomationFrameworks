
from src.com.Utility.Tool import Tool

class TestCaseResult(object):
    """description of class"""

    TestCaseFile:str = None
    TestCaseName:str = None
    TestCaseNumber:str = None
    CaseResult:str = None
    StartTime:str = None
    EndTime:str = None
    TestStateResultCollection:list = None

    def __init__ (self, testCaseFile):
        self.TestCaseFile = testCaseFile
        self.TestCaseName = self.TestCaseFile.replace(".xlsx","")
        self.TestStateResultCollection = []
        self.StartTime = Tool.CurrentTime()

    def TotalCount(self):
        if self.TestStateResultCollection != None:
            return len(self.TestStateResultCollection)
        else:
            return 0