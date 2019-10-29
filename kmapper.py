#!/usr/bin/env python
import sys
import csv
import math

SEP = "\t"

centers=[]
k=5

def computeDist(data, center):
    temp = [(float(data[i]) - float(center[i])) ** 2 for i in range(0, len(data))]
    return (sum(temp))

class Mapper(object):
    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep = sep
        self.count = 0
        
    def emit(self, key, value):
        sys.stdout.write("{}{}{}\n".format(key, self.sep, value))
      
    def map(self):
        for row in self:
            if self.count < k:
                centers.append(row[1:])
            self.count +=1
            minDis = sys.maxsize
            index = -1
            data = row[1:]
            for i in range(len(centers)):               
                dis = computeDist(data,centers[i])
                if dis < minDis:
                    minDis=dis
                    index = 'k' + str(i)
            self.emit(index, str(data).strip('[]'))
        
    def __iter__(self):
        reader = csv.reader(self.stream)
        for row in reader:
            yield row
        
if __name__ == '__main__':
    mapper = Mapper(sys.stdin)
    mapper.map()
            