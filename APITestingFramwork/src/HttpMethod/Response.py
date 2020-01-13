import requests

def getResponseContent(res:requests.Response):
    return res.content

def getResponseStatusCode(res:requests.Response):
    return res.status_code

def getResponseHeaders(res:requests.Response):
    return res.headers

def getResponseText(res:requests.Response):
    return res.text

def getResponseCookies(res:requests.Response):
    return res.cookies

def getResponsReson(res:requests.Response):
    return res.reason