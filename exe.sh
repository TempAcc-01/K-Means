#!/bin/bash
# exe.sh

read -p "Input number of times to iterate: " num


hadoop fs -rm -R /input
hadoop fs -mkdir /input
hadoop fs -put 3D_spatial_network.txt /input


hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /input/3D_spatial_network.txt -output /input/centers -mapper kmapper.py -combiner kcombiner.py -reducer kreducer.py -file kmapper.py -file kcombiner.py -file kreducer.py

hadoop fs -copyToLocal -f /input/centers/part-00000 centers.txt

for((x=1; x<num; x++))
{
cp -f 3D_spatial_network.txt nextiteration.txt
./prepend.py nextiteration.txt centers.txt
mv -f centers.txt centers$x.txt

hadoop fs -put -f nextiteration.txt /input

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /input/nextiteration.txt -output /input/centers$x -mapper kmapper.py -combiner kcombiner.py -reducer kreducer.py -file kmapper.py -file kcombiner.py -file kreducer.py

hadoop fs -copyToLocal -f /input/centers$x/part-00000 centers.txt

if cmp -s "centers.txt" "centers$x.txt"; then
   x=$num
   echo "Centers Found!"
fi
}

