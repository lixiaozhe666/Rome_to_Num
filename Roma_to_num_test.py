# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/03 11:51'

import re  # 正则表达式


# def getRomanNum(RomanStr):
#     '''
#     输入罗马数字字符串，输出转换后的阿拉伯字符串
#     逻辑说明:原本是使用所有规则一个个if来判断处理的,但是这样的代码非常垃圾,学习后改进.
#     使用正则的类似思想,对输入串判断romanpattern中规则出现的情况,
#     例如以MXCVI为例,则在pattern的结果是:^M{1}C{0}XCX{0}VI{1} 1000+90+6这里就可以按照千百十分位来分别判断处理
#     其中retnum则是存放转化后的阿拉伯数字,用于返回.
#     '''
#     # 正则表达式进行匹配,判断输入是否合法,罗马数字一般情况下是自左至右依此变小，而前小后大的情况只有这几种
#     if re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', RomanStr) != None:
#         NumDic = {"pattern": "", "retNum": 0}  # 值记录区
#         # 如测试数为 XCVI 则最后retNum 96 pattern ^M{0}C{0}XCX{0}VI{1} 展示出现数次
#         RomanPattern = {
#             "0": ('', '', '', 'M'),  # 1000
#             "1": ('CM', 'CD', 'D', 'C', 100),  # 900 400 500 100
#             "2": ('XC', 'XL', 'L', 'X', 10),  # 90 40 50 10
#             "3": ('IX', 'IV', 'V', 'I', 1)  # 9 4 5 1
#         }
#         i = 3
#         NumItems = sorted(RomanPattern.items())  # 对字典先排序返回元组
#         print NumItems
#         for RomanItem in NumItems:
#             # print RomanItem
#
#             if RomanItem[0] != '0':  # 先统计千内的,因为千内的RomanPattern与千的不一致
#                 patstr = NumDic["pattern"].join(['', RomanItem[1][0]])
#                 print "R "+patstr
#                 if re.search(patstr, RomanStr) != None:  # 先判断Romanstr中是否存在parstr
#                     NumDic["retNum"] += 9 * RomanItem[1][4]  # +=900
#                     NumDic["pattern"] = patstr  # 存放正则信息
#                 else:
#                     patstr = NumDic["pattern"].join(['', RomanItem[1][1]])
#                     # print patstr
#                     if re.search(patstr, RomanStr) != None:
#                         NumDic["retNum"] += 4 * RomanItem[1][4]  # +=40
#                         NumDic["pattern"] = patstr
#                     else:
#                         patstr = NumDic["pattern"].join(['', RomanItem[1][2]])
#                         if re.search(patstr, RomanStr) != None:
#                             NumDic["retNum"] += 5 * RomanItem[1][4]  # += 50
#                             NumDic["pattern"] = patstr
#             # test
#             # print "retNum " + str(NumDic["retNum"]) ,
#             # print "pattern " +NumDic["pattern"]
#
#             if NumDic["pattern"] == '':
#                 NumDic["pattern"] = '^'  # 拼接正则表达式的开头^
#             tempstr = ''
#             sum = 0
#             for k in range(0, 4):  # 处理连续出现几次的情况  如MMM，CCC等而CM， 'CD', 'D'，'XC', 'XL', 'L'，'IX', 'IV', 'V'永远不会重复出现，前大后小原则所以用for来计算
#                 pstr = RomanItem[1][3].join(['', '{']).join(['', str(k)]).join(['', '}'])#拼接正则表达式
#
#                 patstr = NumDic["pattern"].join(['', pstr])
#                 # print patstr
#                 if re.search(patstr, RomanStr) != None:
#                     sum = k * (10 ** i)
#                     tempstr = patstr
#             if tempstr <> '':  # 不等于即依旧为原始值
#                 NumDic["pattern"] = tempstr
#             else:
#                 NumDic["pattern"] = patstr
#             NumDic['retNum'] += sum
#             i -= 1
#         # print NumDic
#         return NumDic['retNum']
#         # return NumDic['pattern']
#     else:
#         print 'String is not a valid Roman numerals'

def getRomanNum(RomanStr):
    '''
    输入罗马数字字符串，输出转换后的阿拉伯字符串
    逻辑说明:原本是使用所有规则一个个if来判断处理的,但是这样的代码非常垃圾,学习后改进.
    使用正则的类似思想,对输入串判断romanpattern中规则出现的情况,
    例如以MXCVI为例,则在pattern的结果是:^M{1}C{0}XCX{0}VI{1} 1000+90+6这里就可以按照千百十分位来分别判断处理
    其中retnum则是存放转化后的阿拉伯数字,用于返回.
    '''
    # 正则表达式进行匹配,判断输入是否合法,罗马数字一般情况下是自左至右依此变小，而前小后大的情况只有这几种
    if re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', RomanStr) != None:
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
        print NumItems
        for RomanItem in NumItems:
            # print RomanItem

            if RomanItem[0] != '0':  # 先统计千内的,因为千内的RomanPattern与千的不一致
                patstr = NumDic["pattern"].join(['', RomanItem[1][0]])
                print "R "+patstr
                if re.search(RomanItem[1][0], RomanStr) != None:  # 先判断Romanstr中是否存在parstr
                    NumDic["retNum"] += 9 * RomanItem[1][4]  # +=900
                    NumDic["pattern"] = patstr  # 存放正则信息
                else:
                    patstr = NumDic["pattern"].join(['', RomanItem[1][1]])
                    # print patstr
                    if re.search(RomanItem[1][1], RomanStr) != None:
                        NumDic["retNum"] += 4 * RomanItem[1][4]  # +=40
                        NumDic["pattern"] = patstr
                    else:
                        patstr = NumDic["pattern"].join(['', RomanItem[1][2]])
                        if re.search(RomanItem[1][2], RomanStr) != None:
                            NumDic["retNum"] += 5 * RomanItem[1][4]  # += 50
                            NumDic["pattern"] = patstr
            # test
            # print "retNum " + str(NumDic["retNum"]) ,
            # print "pattern " +NumDic["pattern"]

            if NumDic["pattern"] == '':
                NumDic["pattern"] = '^'  # 拼接正则表达式的开头^
            tempstr = ''
            sum = 0
            for k in range(0, 4):  # 处理连续出现几次的情况  如MMM，CCC等而CM， 'CD', 'D'，'XC', 'XL', 'L'，'IX', 'IV', 'V'永远不会重复出现，前大后小原则所以用for来计算
                pstr = RomanItem[1][3].join(['', '{']).join(['', str(k)]).join(['', '}'])#拼接正则表达式

                patstr = NumDic["pattern"].join(['', pstr])
                print patstr
                if re.search(patstr, RomanStr) != None:
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
print getRomanNum('MMMXXX')