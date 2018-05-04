# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/03 18:57'
from Rome_to_num import RomeToNum

class FactoryNumTrans:
    @classmethod
    def ChooseTransType(cls,TransType,filename):
        if TransType =="RomeToNum":
            return RomeToNum(filename)
        else:
            return None