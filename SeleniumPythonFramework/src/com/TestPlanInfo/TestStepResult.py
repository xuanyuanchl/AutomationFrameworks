from src.com.Enumeration.StepResult import StepResult

class TestStepResult(object):
    """description of class"""
    Expect:str = None
    Actual:str = None
    StepKeyword:str = None
    StepNumber:str = None
    StepDescription:str = None
    StepParameter:str = None
    StepTagName:str = None
    StepObject:str = None
    startTime:str = None
    endTime:str = None
    stepLog:str = None
    stepResult:StepResult = None
    def __init__(self):
        self.stepResult = StepResult.NotRun