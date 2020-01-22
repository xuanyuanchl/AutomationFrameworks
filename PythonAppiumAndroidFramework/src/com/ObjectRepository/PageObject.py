class PageObject(object):
    """List path expression of all elements of page1"""

    def __init__(self):
        pass

    def getPageObject(self, objectName):
        if(objectName == "button_7"):
            return {"id": "com.miui.calculator:id/btn_7_s"}
        if(objectName == "button_+"):
            return {"id": "com.miui.calculator:id/btn_plus_s"}
        if(objectName == "button_1"):
            return {"id": "com.miui.calculator:id/btn_1_s"}
        if(objectName == "button_clear"):
            return {"id": "com.miui.calculator:id/btn_c_s"}
        return None
