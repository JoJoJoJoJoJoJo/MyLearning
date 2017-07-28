#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import shutil

Ifcontinue=1
while Ifcontinue==1:
    path1=raw_input ("请输入原始文件夹路径:")
    path2=raw_input ("请输入目标文件夹路径:")

    try:
        Filelist=[x for x in os.listdir(path1)]
        for files in Filelist:
            realpath=os.path.join(path1,files)
            shutil.copy (realpath,path2)
            print "复制文件成功！"
    except IOError,e:
        print "文件路径错误或目标文件夹权限不足"
    except WindowsError,e:
        print '文件路径错误'
    finally:
        try:
            Ifcontinue=int(raw_input("是否继续？1=继续"))
        except:
            Ifcontinue=0
