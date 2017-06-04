#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'test module'

__author__ = 'dwj'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _privateTest():
    print('this is private test')
    
#当该module导入到其他模块后,if失效;此功能常用于测试
#原因:当模块是被直接调用执行的，取值为模块的名字；当模块是直接执行的，则该变量取值为__main__
if __name__=='__main__':
    test()