#!/usr/bin/env python

import sys
import csv
import math

from itertools import islice
from itertools import groupby
from operator import itemgetter

SEP= "\t"

clusterSum=[]

class Reducer(object):
    
    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep = sep
        
    def emit(self, key, value):
        sys.stdout.write("{}{}{}\n".format(key, self.sep, value))
        
    def reduce(self):
        for current, group in groupby(self, itemgetter(0)):
            clusterCent=[]
            totalA=0
            totalB=0
            totalC=0
            NUM=0
            
            for item in group:
                totalA += float(item[1][0])
                totalB += float(item[1][1])
                totalC += float(item[1][2])
                NUM += int(item[1][3])
            
            clusterCent.append(totalA/NUM)
            clusterCent.append(totalB/NUM)
            clusterCent.append(totalC/NUM)
            self.emit(current, clusterCent)
    
    def __iter__(self):
        for line in self.stream:
            try:
                parts=line.split(self.sep)
                yield parts[0], eval(parts[1])
            except:
                continue

if __name__ == '__main__':
    reducer = Reducer(sys.stdin)
    reducer.reduce()
    