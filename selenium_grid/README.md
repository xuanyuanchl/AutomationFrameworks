## 环境准备

-  java安装，以及环境配置
- python 3.4环境
- selenium安装 ```pip install selenium```
- Chromedriver 要和本地的chrome浏览器匹配,[点击下载](http://npm.taobao.org/mirrors/chromedriver/)
- 下载selenium-server-standalone[点击下载](http://selenium-release.storage.googleapis.com/index.html)
- 准备2台pc，如果是虚拟机，选择桥接，2台pc互相能ping通,本次测试为本机

## 开始部署

- **启动hub**

```
 java -jar selenium-server-standalone-v3.0.1.jar -role hub -port 4455
```
![image.png](https://upload-images.jianshu.io/upload_images/2231755-518068925e34a67f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- **启动node**

```
java -jar selenium-server-standalone-v3.0.1.jar -role node -port 5555 -hub http://192.168.0.102:4444/grid/registe

java -jar selenium-server-standalone-v3.0.1.jar -role node -port 6666 -hub http://192.168.0.102:4444/grid/registe
```
![image.png](https://upload-images.jianshu.io/upload_images/2231755-5e5aced2098f2235.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 其他node启动方式

```
java -Dwebdriver.ie.driver=D:\IEDriverServer.exe -jar selenium-server-standalone-2.37.0.jar -role node -hub [http://127.0.0.1:4444/grid/register](http://127.0.0.1:4444/grid/register) -maxSession 20 -browser "browserName=internet explorer,version=9,platform=WINDOWS,maxInstances=20" -port 5555

```
node是只运行IE，并且并发数是20，最多有20个IE浏览器在运行

## 查看grid信息

浏览器打开：```http://hub_ip:4444/grid/console ```可以查看hub信息，和已经连上的node信息
![image.png](https://upload-images.jianshu.io/upload_images/2231755-5f8f408224c60d02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 运行
- test.py