# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/03 14:00'

from Factory import FactoryNumTrans
temp = FactoryNumTrans.ChooseTransType("RomeToNum","test-data/test.txt")
temp.printResult()