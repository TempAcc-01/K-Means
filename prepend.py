#!/usr/bin/env python

import sys
import csv
import re

SEP = "\t"

def line_pre_adder(file1, file2):
    f1_read=open(file1,'r')
    buff=f1_read.read()
    f1_read.close()
    f2_read=open(file2,'r')
    text=f2_read.read()
    text=text.replace(SEP,',').replace('[','').replace(']','').replace(' ','')
    print(text)
    f2_read.close()
    f_write=open(file1,'w')
    inj_pos=0
    f_write.write(buff[:inj_pos]+text+buff[inj_pos:])
    f_write.close()
                      
if __name__ == '__main__':
    line_pre_adder(sys.argv[1],sys.argv[2])
    