#!/bin/bash

mkdir output
read -p "Input number of times to iterate: " num
cat 3D_spatial_network.txt | ./kmapper.py | sort | ./kcombiner.py | ./kreducer.py > output/centers0.txt

for((x=1; x<num; x++))
{
y=$(($x-1))
echo $y
cp -f 3D_spatial_network.txt nextiteration.txt
./prepend.py nextiteration.txt output/centers$y.txt
cat nextiteration.txt | ./kmapper.py | sort | ./kcombiner.py | ./kreducer.py > output/centers$x.txt

if cmp -s "output/centers$x.txt" "output/centers$y.txt"; then
   x=$num
   echo "Centers Found!"
fi

}
exit 0
