# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/03 14:15'
import fileinput
class NumTransformation:
    def __init__(self,filename):
        self.filename = filename

    def getSourceNum(self,souceNum):
        pass

    def str_Resolve(input_line):
        pass

    def printResult(self):
        with open("test-data/test.txt") as txtData:
            lines = txtData.readlines()
            for line in lines:
                try:
                    str_return = self.str_Resolve(line)
                    if str_return:
                        print str_return
                except:
                    print "I have no idea what you are talking about"

