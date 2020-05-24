from collections import Counter
from src.com.Utility.Tool import Tool

class TestPlanResult(object):
    """description of class"""
    TestPlanStartTime:str = None
    TestPlanEndTime:str = None
    TestPlan:str = None
    TestCaseResultCollection:list = None
    allScenarioPassedCount:int = 0
    allScenarioFailedCount:int = 0
    moduleInfoCollection:dict = None
    allScenarioPassPercentage:str = None
    allScenarioFailPercentage:str = None

    def __init__ (self, TestPlanFile):
        self.TestCaseResultCollection = []
        self.TestPlanStartTime = Tool.CurrentTime()
        self.TestPlan = TestPlanFile

    def setAllScenarioPassFailInfo(self):
        for x in self.TestCaseResultCollection:
            if x.CaseResult == 'Passed':
                self.allScenarioPassedCount = self.allScenarioPassedCount + 1
            else:
                self.allScenarioFailedCount = self.allScenarioFailedCount + 1
        self.allScenarioPassPercentage = "width:" + str((self.allScenarioPassedCount / (self.allScenarioPassedCount + self.allScenarioFailedCount) * 100)) + "%"
        self.allScenarioFailPercentage = "width:" + str((self.allScenarioFailedCount / (self.allScenarioPassedCount + self.allScenarioFailedCount) * 100)) + "%"
    
    def getModuleInfo(self):
        TestScenarioCollection = []
        for x in self.TestCaseResultCollection:
            TestScenarioCollection.append(x.TestCaseFile)
        self.moduleInfoCollection = {}
        # Module1\LaunchBaiduAndSearch.xlsx
        testModuleList:list = []
        for TestScenario in TestScenarioCollection:
            testModuleList.append(TestScenario.split('\\')[0])
        self.moduleInfoCollection = self.groupBy(testModuleList)

    @property
    def TotalCount(self):
        if self.TestCaseResultCollection != None:
            return len(self.TestCaseResultCollection)
        else:
            return 0

    def groupBy(self, collections):
        cou = Counter(collections)
        li = sorted(cou)
        d = {}
        for key in li:
            d[key] = cou[key]
        return d
