#!/usr/bin/env python3
#--coding:utf-8--
"""
word.py
Nature Language Processing basic code.
全角字符unicode编码从65281~65374 （十六进制 0xFF01 ~ 0xFF5E）
半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）
空格比较特殊，全角为 12288（0x3000），半角为 32（0x20）
除空格外，全角/半角按unicode编码排序在顺序上是对应的（半角 + 0x7e= 全角）,所以可以直接通过用+-法来处理非空格数据，对空格单独处理。
一些标点符号的全角半角转换有问题，因而额外加了处理。
2018-06-28: basically finished.
"""

import re


def isChineseChar(c):
    if c >= u'\u4e00' and c <= u'\u9fa5':
        return True
    return False


def containChineseString(s):
    for c in s:
        if isChineseChar(c):
            return True
    return False


def extractChinese(s):
    """
    s is str
    """
    s = str(s)
    ns = ""
    for t in s:
        if isChineseChar(t):
            ns += t
    if len(ns) == 0:
        return None
    return ns

def isNumberChar(c):
    if c >= u'\u0030' and c <= u'\u0039':
        return True
    return False


def containNumberString(s):
    for c in s:
        if isNumberChar(c):
            return True
    return False


def isAlphabetChar(c):
    if (c >= u'\u0041' and c <= u'\u005a') or \
        (c>=u'\u0061' and c<= u'\u007a'):
        return True
    return False


def containAlphabetString(s):
    for c in s:
        if isAlphabetChar(c):
            return True
    return False


def q2bChar(c):
    """
    全角转半角
    """
    ic = ord(c)
    if ic == 0x3000:
        ic = 0x0020
    else:
        ic -= 0xfee0
    if ic < 0x0020 or ic > 0x7e:
        return c
    return chr(ic)


def q2bString(s):
    ns = "".join([q2bChar(c) for c in s])
    return ns


def b2qChar(c):
    """
    半角转全角
    """
    ic = ord(c)
    if ic < 0x0020 or ic > 0x7e:
        return c
    if ic == 0x0020:
        ic = 0x3000
    else:
        ic += 0xfee0
    return chr(ic)


def b2qString(s):
    ns = "".join([b2qChar(c) for c in s])
    return ns



def q2bSymbolString(s):
    pattern = re.compile('[，。：“”【】《》？；、（）‘’『』「」﹃﹄〔〕—·％＃＠＆]')
    fps = re.findall(pattern, s)
    if len(fps) > 0:
        s = s.replace('，', ',')
        s = s.replace('。', '.')
        s = s.replace('：', ':')
        s = s.replace('“', '"')
        s = s.replace('”', '"')
        s = s.replace('【', '[')
        s = s.replace('】', ']')
        s = s.replace('《', '<')
        s = s.replace('》', '>')
        s = s.replace('？', '?')
        s = s.replace('；', ':')
        s = s.replace('、', ',')
        s = s.replace('（', '(')
        s = s.replace('）', ')')
        s = s.replace('‘', "'")
        s = s.replace('’', "'")
        s = s.replace('’', "'")
        s = s.replace('『', "[")
        s = s.replace('』', "]")
        s = s.replace('「', "[")
        s = s.replace('」', "]")
        s = s.replace('﹃', "[")
        s = s.replace('﹄', "]")
        s = s.replace('〔', "{")
        s = s.replace('〕', "}")
        s = s.replace('—', "-")
        s = s.replace('·', ".")
        s = s.replace('％', "%")
        s = s.replace('＃', "#")
        s = s.replace('＠', "@")
        s = s.replace('＆', "&")
    return q2bString(s)


def test():
    a = "我"
    b = "I"
    c = "20"
    print(isChineseChar(a))
    print(isChineseChar(b))
    print(isChineseChar(c))
    print()
    print(isNumberChar(a))
    print(isNumberChar(b))
    print(isNumberChar(c))
    print()
    print(isAlphabetChar(a))
    print(isAlphabetChar(b))
    print(isAlphabetChar(c))
    print()
    d = "我今年20 years old"
    print(containChineseString(d))
    print(containNumberString(d))
    print(containAlphabetString(d))
    print()
    e = ".。，：a, 2!！^[‘“'"
    f = q2bString(e)
    print(e)
    print(f)
    print(b2qString(f))
    print(q2bString((q2bSymbolString(e))))


if __name__ == "__main__":
    test()
