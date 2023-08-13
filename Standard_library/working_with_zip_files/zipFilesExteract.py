from zipfile import ZipFile

with ZipFile("C:/Users/Dell/Desktop/test/files.zip",'r') as zObject:
    zObject.extractall("C:/Users/Dell/Desktop/test")