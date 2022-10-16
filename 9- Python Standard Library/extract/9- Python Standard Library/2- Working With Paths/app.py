# from os import path
from pathlib import Path

# path = Path(r"C:\Program Files\Microsoft")
# path = Path()
path = Path.home()
# path = Path() / "ecommerce" / "__init__.py"
# path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
# print(path)
# path = path.with_name("file.txt")
print(path)
print(path.absolute())
# path = path.with_suffix(".txt")
