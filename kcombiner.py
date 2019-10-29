#!/usr/bin/env python

import sys
import csv
import math

from itertools import islice
from itertools import groupby
from operator import itemgetter

SEP= "\t"

class Combiner(object):
    
    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep = sep
        
    def emit(self, key, value):
        sys.stdout.write("{}{}{}\n".format(key, self.sep, value))
        
    def combine(self):
        for current, group in groupby(self, itemgetter(0)):
            clusterSum=[]
            totalX=0
            totalY=0
            totalZ=0
            count=0
            
            for item in group:
                totalX += float(item[1][0])
                totalY += float(item[1][1])
                totalZ += float(item[1][2])
                count += 1
            
            clusterSum.append(totalX)
            clusterSum.append(totalY)
            clusterSum.append(totalZ)
            clusterSum.append(count)
            self.emit(current, clusterSum)
            
    def __iter__(self):
        for line in self.stream:
            try:
                parts=line.split(self.sep)
                yield parts[0], eval(parts[1])
            except:
                continue

if __name__ == '__main__':
    combine = Combiner(sys.stdin)
    combine.combine()