# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/03 14:33'
from Numerical_transformation import NumTransformation
import re

class RomeToNum(NumTransformation):
    def __init__(self,filename):
        self.Romanarray = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        self.word_dic = {}  # 以字典来对应单词和罗马数字
        self.coin_dic = {}  # 以字典来对应货币和价值
        self.filename = filename
    def getSourceNum(self,souceNum):
        if re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',souceNum) != None:
            NumDic = {"pattern": "", "retNum": 0}  # 值记录区
            # 如测试数为 XCVI 则最后retNum 96 pattern ^M{0}C{0}XCX{0}VI{1} 展示出现数次
            RomanPattern = {
                "0": ('', '', '', 'M'),  # 1000
                "1": ('CM', 'CD', 'D', 'C', 100),  # 900 400 500 100
                "2": ('XC', 'XL', 'L', 'X', 10),  # 90 40 50 10
                "3": ('IX', 'IV', 'V', 'I', 1)  # 9 4 5 1
            }
            i = 3
            NumItems = sorted(RomanPattern.items())  # 对字典先排序返回元组
            # print NumItems
            for RomanItem in NumItems:
                # print RomanItem
                if RomanItem[0] != '0':  # 先统计千内的,因为千内的RomanPattern与千的不一致
                    patstr = NumDic["pattern"].join(['', RomanItem[1][0]])
                    # print "R "+RomanItem[1][0]
                    if re.search(patstr, souceNum) != None:  # 先判断souceNum中是否存在parstr
                        NumDic["retNum"] += 9 * RomanItem[1][4]  # +=90
                        NumDic["pattern"] = patstr  # 存放正则信息
                    else:
                        patstr = NumDic["pattern"].join(['', RomanItem[1][1]])
                        # print patstr
                        if re.search(patstr, souceNum) != None:
                            NumDic["retNum"] += 4 * RomanItem[1][4]  # +=40
                            NumDic["pattern"] = patstr
                        else:
                            patstr = NumDic["pattern"].join(['', RomanItem[1][2]])
                            if re.search(patstr, souceNum) != None:
                                NumDic["retNum"] += 5 * RomanItem[1][4]  # += 50
                                NumDic["pattern"] = patstr
                # test
                # print "retNum " + str(NumDic["retNum"]) ,
                # print "pattern " +NumDic["pattern"]

                if NumDic["pattern"] == '':
                    NumDic["pattern"] = '^'  # 拼接正则表达式的开头^
                tempstr = ''
                sum = 0
                for k in range(0,
                               4):  # 处理连续出现几次的情况  如MMM，CCC等而CM， 'CD', 'D'，'XC', 'XL', 'L'，'IX', 'IV', 'V'永远不会重复出现，前大后小原则所以用for来计算
                    pstr = RomanItem[1][3].join(['', '{']).join(['', str(k)]).join(['', '}'])  # 拼接正则表达式

                    patstr = NumDic["pattern"].join(['', pstr])
                    # print patstr
                    if re.search(patstr, souceNum) != None:
                        sum = k * (10 ** i)
                        tempstr = patstr
                if tempstr <> '':  # 不等于即依旧为原始值
                    NumDic["pattern"] = tempstr
                else:
                    NumDic["pattern"] = patstr
                NumDic['retNum'] += sum
                i -= 1
            # print NumDic
            return NumDic['retNum']
            # return NumDic['pattern']
        else:
            print 'String is not a valid Roman numerals'

    def str_Resolve(self,input_line):
        if input_line[-1] =="\n":
            input_line = input_line[:-1]
        if input_line[-1] in self.Romanarray:
            input_line_array = input_line.split(' ')  # 以空格截取
            self.word_dic[input_line_array[0]] = input_line_array[2]  # 取第一个和最后一个元素
            return
            # print 'word_dic:',word_dic:

        elif input_line[-1] == 's':  # 以小写ｓ做为金币银币那些测试数据的识别符号
            input_line_array = input_line.split(' ')  # 以空格截取

            temp_str = ''
            for i in range(len(input_line_array) - 4):
                temp_str += self.word_dic[input_line_array[i]]

            temp_num = self.getSourceNum(temp_str)
            # print "input_line_array[-4]",input_line_array[-4]
            self.coin_dic[input_line_array[-4]] = int(input_line_array[-2]) / int(temp_num)
            return
            # print 'coin_dic:',coin_dic

        elif input_line[-1] == '?':  # 以?为标志,判断是否是第三四类输入
            input_line_array = input_line.split(' ')
            # print "input_line_array:",input_line_array

            if input_line_array[1] == 'much':
                temp_str1 = ''
                temp_str3 = ''
                if input_line_array[2] =='is':
                    for i in range(3, len(input_line_array) - 1):  # 抽取第四个到最后一个数组元素
                        temp_str3 += input_line_array[i] + ' '
                        temp_str1 += self.word_dic[input_line_array[i]]

                    return temp_str3 + "is " + str(self.getSourceNum(temp_str1))  # 转化成数字并且输出
                else:
                    print "I have no idea what you are talking about"


            elif input_line_array[1] == 'many':  # 处理ｍａｎｙ
                temp_str2 = ''
                temp_str4 = ''
                for i in range(4, len(input_line_array) - 2):  # 取第５个到倒数第三个之间
                    temp_str4 += input_line_array[i] + ' '
                    temp_str2 += self.word_dic[input_line_array[i]]  # 转化为字符进行ｒｏｍａ查询

                return temp_str4 + input_line_array[-2] + ' is ' + str(
                    self.coin_dic[input_line_array[-2]] * self.getSourceNum(temp_str2)) + ' Credits'  # 输出数量＊单位价值
