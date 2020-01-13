class PageObject(object):
    """List path expression of all elements of page1"""
    def __init__(self):
        pass

    def getPageObject(self, objectName):
        if(objectName=="baidu_search_box"):
            return {"id":"kw"}
        if(objectName=="baidu_search_button"):
            return {"id":"su"}
        return None