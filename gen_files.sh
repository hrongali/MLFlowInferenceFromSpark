#!/bin/bash

num_files=$1
STORAGE=`grep -A1 'hive.metastore.warehouse.dir' /etc/hive/conf/hive-site.xml | grep value | sed 's/<value>//g' | sed 's/<\/value>//g' | cut -d '/' -f1,2,3`

hadoop fs -rm -r $STORAGE/tmp/*

get_tokens() {
    str=''
    for token in {0..24}
    do
       str=$str$((RANDOM%10 + 1)).0','
    done
    echo $str | sed 's/.$//'
}

cd /home/cdsw/data


for i in $( seq 0 $num_files )
do
     echo $i
     sleep 3
     for row in {0..11}
     do
         get_tokens >> file$i
     done
     
     hadoop fs -put file$i $STORAGE/tmp/
done