from com.TestSettings.Settings import Settings

class TestModuleInfo(object):
    """description of class"""
    currentModuleName = None
    moduleScriptCount:int = 0
    moduleScriptPassedCount:int = 0
    moduleScriptFailedCount:int = 0
    modulePassPercentage:str = ''
    moduleFailPercentage:str = ''      

    def setModuleName(self, moduleName:str):
        self.currentModuleName = moduleName

    def setModuleInfo(self):
        self.settings = Settings.getSettings()
        self.moduleScriptCount = self.settings.testPlanResult.moduleInfoCollection[self.currentModuleName]
        for testCaseR in self.settings.testPlanResult.TestCaseResultCollection:
            if testCaseR.TestCaseFile.split('\\')[0] == self.currentModuleName:
                if testCaseR.CaseResult == "Passed":
                    self.moduleScriptPassedCount = self.moduleScriptPassedCount + 1
                else:
                    self.moduleScriptFailedCount = self.moduleScriptFailedCount + 1
        self.modulePassPercentage = "width:" + str((self.moduleScriptPassedCount / (self.moduleScriptPassedCount + self.moduleScriptFailedCount) * 100)) + "%"
        self.moduleFailPercentage = "width:" + str((self.moduleScriptFailedCount / (self.moduleScriptPassedCount + self.moduleScriptFailedCount) * 100)) + "%"