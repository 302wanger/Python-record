# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os

class ImageSpider(object):
    """docstring for ClassName"""

    num = 0;

    def __init__(self):
        pass

    def saveImage(self, imageUrl, imageName):
        imageData = urllib.urlopen(imageUrl).read()
        f = open(imageName, 'w')
        f.write(imageData)
        print '正在保存图片：', imageName
        f.close()


    def getImageFormUrl(self, url):
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        response = urllib2.urlopen(url)
        text = response.read()

        pattern = re.compile(r'<span>.*?img.*?alt="(.*?)".*?src="(.*?)".*?>.*?</span>', re.S)
        imgs = re.findall(pattern, text)

        for img in imgs:
            imageName = "images/%d_%s.png" % (ImageSpider.num, img[0])
            imageUrl = img[1]
            self.saveImage(imageUrl, imageName)
            ImageSpider.num += 1


    def getImagePageRange(self, fromPage, toPage):

        os.system('mkdir images')    #创建保存图片的目录

        i = int(fromPage)
        while i <= int(toPage):
            url = "http://www.dbmeinv.com/dbgroup/show.htm?pager_offset=" + str(i)
            print "\n第%d页" % i
            self.getImageFormUrl(url)
            i += 1

imageSpider = ImageSpider()
beginPage = raw_input("输入开始页：")
endPage = raw_input("输入结束页：")
imageSpider.getImagePageRange(beginPage, endPage)
