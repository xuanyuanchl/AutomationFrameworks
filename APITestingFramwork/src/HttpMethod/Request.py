import requests

def httpGet(url, params=None, **kwargs):
    try:
        respon:Response = requests.get(url,params=params,**kwargs)
        respon.raise_for_status()
    except requests.HTTPError as e:
        return str(e)
    except Exception as e:
        return str(e)
    else:
        return respon

def httpPost(url, data = None, json = None, **kwargs):
    try:
        respon:Response = requests.post(url, data = data, json = json,**kwargs)
        respon.raise_for_status()
    except requests.HTTPError as e:
        return str(e)
    except Exception as e:
        return str(e)
    else:
        return respon

def httpPut(url, data = None, **kwargs):   
    try:
        respon:Response = requests.put(url, data = data, **kwargs)
        respon.raise_for_status()
    except requests.HTTPError as e:
        return str(e)
    except Exception as e:
        return str(e)
    else:
        return respon

def httpDelete(url, **kwargs):   
    try:
        respon:Response = requests.delete(url, **kwargs)
        respon.raise_for_status()
    except requests.HTTPError as e:
        return str(e)
    except Exception as e:
        return str(e)
    else:
        return respon

def httpHead(url, **kwargs):   
    try:
        respon:Response = requests.head(url, **kwargs)
        respon.raise_for_status()
    except requests.HTTPError as e:
        return str(e)
    except Exception as e:
        return str(e)
    else:
        return respon  
      
def httpOptions(url, **kwargs):   
    try:
        respon:Response = requests.options(url, **kwargs)
        respon.raise_for_status()
    except requests.HTTPError as e:
        return str(e)
    except Exception as e:
        return str(e)
    else:
        return respon       

# url1 = 'http://www.webxml.com.cn/WebServices/RandomFontsWebService.asmx/getCharFonts?byFontsLength={0}'.format('6')
# print (httpGet(url1))
# 
# url2 = 'http://www.webxml.com.cn/WebServices/RandomFontsWebService.asmx/getCharFonts'
# data:dict = {'byFontsLength':'6'}
# print (httpPost(url1,data))