from pathlib import Path
from zipfile import ZipFile

with ZipFile("file.zip", "w") as zip:
    for p in Path("9- Python Standard Library").rglob("*.*"):
        zip.write(p)


with ZipFile("file.zip") as zip:
    print(zip.namelist())
