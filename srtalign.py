import os
import pysrt

data = ""

nData = ""

NAME = "-已拉满"

# 获取该py文件的目录
dirname = os.path.dirname(__file__)


# 在字符串指定位置添加字符串
def insert_string(original, insert, position):
    return original[:position] + insert + original[position:]


# 获取srt文件的绝对路径
def getDrtFilePath(dirname: str):
    for tmp in os.listdir(dirname):
        # print(tmp)
        if "srt" in tmp and NAME not in tmp:
            return dirname + "\\" + tmp


srtFile = getDrtFilePath(dirname)

subs = pysrt.open(srtFile, encoding="utf-8")
i = 0
length = len(subs)

nSubs = subs

for sub in subs:
    if i < length - 1:
        nSubs[i].end = subs[i + 1].start
        i = i + 1
    else:
        i = 0

# 建立新srt文件
position = len(srtFile) - 4  # srt后缀长度
result = insert_string(srtFile, NAME, position)

nSubs.save(result, encoding="utf-8")
