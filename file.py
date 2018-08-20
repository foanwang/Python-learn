import sys
#coding=UTF8
filename =  input('請輸入檔名:')
file = open(filename, 'r', encoding = 'UTF-8')
while True:
    line = file.readline()
    if not line: break
    print(line, end='')
file.close
