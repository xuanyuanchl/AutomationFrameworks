from src.com.TestSettings.Settings import Settings
from src.com.Utility.Tool import Tool

class TestStateResult(object):
    """update information in state file"""
    TestStateDescription:str = None
    TestStateEndTime:str = None
    TestStateFile:str = None
    TestStateNumber:int = None
    StateResult:str = None
    Attachment:str = None
    StateLog:str = None

    def __init__ (self, tsFile):
        self.TestStepResultCollection:list = []
        self.TestStateFile = tsFile
        self.settings = Settings.getSettings()
        self.TestStateStartTime = Tool.CurrentTime()
        self.TestStateReportPath:str = self.settings.CurrentScriptResultFolder + '\\' + self.TestStateFile.replace('.xlsx', '.html')
        self.RelativeTestStateReportPath:str = self.settings.CurrentScript + '\\' + self.TestStateFile.replace('.xlsx', '.html')

    def setLog(self):
        self.TestStateEndTime:str = Tool.CurrentTime()
        if self.StateResult == 'Passed' :
            self.StateLog =  self.TestStateEndTime + ' Set state passed'
        elif self.StateResult == 'Failed' :
            self.StateLog =  self.TestStateEndTime + ' Set state failed'
        elif self.StateResult == 'Error' :
            self.StateLog =  self.TestStateEndTime + ' Set state, error occurred'
        else:
            self.StateLog =  self.TestStateEndTime + ' Set state, not run'
        return self.StateLog