from pathlib import Path

path = Path('C:\\Users\\Dell\\Documents\\GitHub\\python')
# path.mkdir()
# print(path.parent)
# path.rename("amir")
# print(path.exists())

# print(path.absolute())

# print(path.name)
# print(path.exists())
# path.rmdir()
# print(path.exists())

# paths = [print(p) for p in path.iterdir() if p.is_dir()]

# py_files = [print(p) for p in path.glob("*.py")]

# recur_py_files = [print(p) for p in path.rglob("*.py")] 














# from time import ctime
# print(ctime(path.stat().st_ctime)) # return time of creation
# path = Path("C:\\Users\\Dell\\Documents\\GitHub\\PYTHON_MODULE\\package2\\module4.py")
# with open("C:\\Users\\Dell\\Documents\\GitHub\\PYTHON_MODULE\\package2\\module4.py") as file:
#     print(file.read())
# print(path.read_bytes())
# print(path.read_text()) # return string with content of file 

# path.write_text("import os\nprint(os.getcwd())") # create file with content
# # path.

# # import shutil

# source = Path("C:\\Users\\Dell\\Documents\\GitHub\\PYTHON_MODULE\\package2\\module4.py")
# print(source.read_text())
# target = Path("C:\\Users\\Dell\\Documents\\GitHub\\PYTHON_MODULE\\package2\\module3.py") 
# print(target.read_text())
# # shutil.copy(source,target)
# target.write_text(source.read_text()) # copy file