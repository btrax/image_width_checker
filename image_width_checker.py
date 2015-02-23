#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
# This script check image under current directory width recursively
# python image_width_checker.py {min width} 
import PIL.Image
import os
import os.path
import sys

# get all file list recursively 
def GetFileList(targetDir):

    def FileOrDir(targetDir):
        tmp = os.listdir(targetDir)
        files = []
        dir = []

        for i in range(len(tmp)):
            if os.path.isdir(targetDir+'/'+tmp[i]):
                dir.append(targetDir+'/'+tmp[i])
            else:
                # ignore DS_store
                if ".DS_Store" != tmp[i]:
                    files.append(targetDir+'/'+tmp[i])
         
        return dir,files

    dir,files = FileOrDir(targetDir)
    while (dir != []):
        addDir,addFiles = FileOrDir(dir.pop())
        dir = dir + addDir
        files = files + addFiles
    return files

if __name__ == '__main__':

    # ext(.ext) is image or not
    def isImage(ext):
        if ext in ('.jpg', '.jpeg', '.JPG', '.JPEG', '.GIF', '.gif', '.png', '.PNG') :
            return True
        else:
            return False

    ngList = []
    okList = []

    targetPath = '.'
    files = GetFileList(targetPath)

    # command line params
    argvs = sys.argv
    minWidth = 700  # default
    if len(argvs) != 1: 
        minWidth = int(argvs[1])

    print '----------------' # line break
    print '----CHECK START-----'
    print '----------------' # line break

    for file in files:
        ext = os.path.splitext(file)[1]

        print file
        if isImage(ext):
            f = PIL.Image.open(file)
            width = f.size[0]
            if width < minWidth:
                print 'NG. small!! size:', 
                ngList.append(file)
            else:
                okList.append(file)
                print 'OK. large size:',

            print width
        else:
            print u'NOT TARGET ' + ext + u'is not image'

        print '' # line break

    print '----------------' # line break
    print '----CHECK END-----'
    print '----------------' # line break

    print '----------------' # line break
    print '----OK LIST-----'
    print '----------------' # line break
    print u'count:' + str(len(okList))
    for ok in okList:
       print ok 

    print '----------------' # line break
    print '----NG LIST-----'
    print '----------------' # line break
    print u'count:' + str(len(ngList))
    for ng in ngList:
       print ng