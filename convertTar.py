#coding=utf-8
import os
import sys


def reconsitution(standardTar, originalTar):
    workPath = os.path.split(standardTar)[0]
    targetName = os.path.split(originalTar)[1].replace(".tar", "")
    deleteChildFolder(workPath)
    tmpPath = os.path.join(workPath, "tmpFolder")
    os.mkdir(tmpPath)

    #extract standardTar to tmpPath
    uncompress(standardTar, tmpPath)
    os.rename(os.path.join(tmpPath, os.listdir(tmpPath)[0]), os.path.join(tmpPath, "tmpFolder"))#rename

    #extract tmpPath/tmpFolder/images/, delete img first
    os.remove(os.path.join(tmpPath, "tmpFolder", "images", "userdata.img"))
    uncompress(originalTar, workPath)
    deleteDirs(originalTar)
    copyFile(searchFile(os.path.join(workPath, "home"), "userdata.img"), os.path.join(tmpPath, "tmpFolder", "images"))

    #rename, compress
    os.rename(os.path.join(tmpPath, "tmpFolder"), os.path.join(tmpPath, targetName))
    os.chdir(tmpPath)
    os.system("tar cvf " + os.path.join(workPath, targetName + ".tar") + " " + targetName)
    os.chdir(workPath)


def searchFile(root, filename):
    for element in os.listdir(root):
        absolutePath = os.path.join(root, element)
        if element == filename:
            return absolutePath
        if os.path.isdir(absolutePath):
            return searchFile(absolutePath, filename)


def deleteDirs(path):
    os.system("rm -rf " + path)


def copyFile(source, target):
    os.system("cp " + source + " " + target)


def deleteChildFolder(path):
    folders = os.listdir(path)
    for folder in folders:
        tmp = os.path.join(path, folder)
        if os.path.isdir(tmp):
            deleteDirs(tmp)


def uncompress(source, target):
    os.system("tar -xvf " + source + " -C " + target)


if __name__ == "__main__":
    mPath = sys.argv[1]
    tars = os.listdir(mPath)
    list = [None, None, None, None]#[standard, cm, cu, ct]

    for tar in tars:
        if tar.endswith(".tar"):
            carrier = tar.split("_")[1]
            if carrier == "images":
                list[0] = tar
            elif carrier == "chinamobile" or carrier == "cm":
                list[1] = tar
            elif carrier == "chinaunicom" or carrier == "cu":
                list[2] = tar
            elif carrier == "chinatelecom" or carrier == "ct":
                list[3] = tar
    print list

    #Check standard Tar exist
    if list[0] is None:
        print "Standard TAR doesn't exist!!! "
        sys.exit(0)

    i = 1
    while i < 4:
        if list[i] is not None:
            reconsitution(os.path.join(mPath, list[0]), os.path.join(mPath, list[i]))
            print list[i] + " has been recombined."
        i += 1

    deleteChildFolder(mPath)



