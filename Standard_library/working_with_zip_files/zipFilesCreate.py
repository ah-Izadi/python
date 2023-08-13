# ------------- working with zip files -------------
from pathlib import Path
from zipfile import ZipFile
with ZipFile("C:/Users/Dell/Desktop/test/files.zip", "w") as zip:
    for path in Path("D:/arduio/").rglob("*.*"):
        zip.write(path)