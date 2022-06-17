import os
import time
import json
import requests
import xml.etree.ElementTree as ET
import datetime
import yaml


#Extracting the correct URL from hive-site.xml
tree = ET.parse('/etc/hadoop/conf/hive-site.xml')
root = tree.getroot()

for prop in root.findall('property'):
    if prop.find('name').text == "hive.metastore.warehouse.dir":
        storage = prop.find('value').text.split("/")[0] + "//" + prop.find('value').text.split("/")[2]

print("The correct Cloud Storage URL is:{}".format(storage))

os.environ['STORAGE'] = storage

!echo $STORAGE
!hdfs dfs -rm -r $STORAGE/tmp
!hdfs dfs -rm -r $STORAGE/chkpnt
!hdfs dfs -rm -r $STORAGE/output
!hdfs dfs -mkdir $STORAGE/tmp
!hdfs dfs -mkdir $STORAGE/chkpnt
!hdfs dfs -mkdir $STORAGE/output