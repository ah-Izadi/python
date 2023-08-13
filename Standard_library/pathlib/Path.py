from pathlib import Path

Path("D:\\arduino\\")

Path("D:\\arduino\\dht_11.py")

Path.home()

#make new object from Path class
path = Path("D:\\arduino\\dht_11.py")

#this method return true
print(path.exists())

#this method return true if path is file
print(path.is_file())

#this method return true is path is directory
print(path.is_dir())

# this method return name of path
print(path.name)

# this method return name of path without suffix
print(path.stem)

# this method return suffix of path
print(path.suffix)

# this method return parent directory of path
print(path.parent)


path2 = path.with_name("file.txt")
print(path2)
print(path.absolute())
path3 = path.with_suffix(".py")
print(path3)