from django.test import TestCase
import zipfile
import tempfile
import os
from django.conf import settings
import SecuritySystem
# Create your tests here.
record_dir = 'C:\\Users\\dahyo\\PycharmProjects\\SecuritySystem\\media\\Recordings'
os.chdir(record_dir)

zipObj = zipfile.ZipFile('Records.zip', 'w')
files = os.listdir()

for file in files:
    if file[-4:] == ".mkv":
        zipObj.write(file)
    else:
        continue
zipObj.close()



# zipObj = zipfile.ZipFile('Records.zip', 'w')
