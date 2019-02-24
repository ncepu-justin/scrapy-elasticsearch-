# -*- coding: utf-8 -*-
__author__ = 'justin'
import hashlib
import re


def get_md5(url):
    if isinstance(url, str):        #isinstance() 与 type() 区别：type() 不会认为子类是一种父类类型，不考虑继承关系。isinstance() 会认为子类是一种父类类型，考虑继承关系。如果要判断两个类型是否相同推荐使用 isinstance()
        url = url.encode("utf-8")   #python3 所有字符编码都为unicode
    m = hashlib.md5()               #hash函数不接受unicode编码
    m.update(url)
    return m.hexdigest()


def extract_num(text):
    # 从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


if __name__ == "__main__":
    print(get_md5("http://jobbole.com".encode("utf-8")))
