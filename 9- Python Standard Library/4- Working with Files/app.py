from pathlib import Path
from time import ctime
import shutil


path = Path(
    """9- Python Standard Library/4- Working with Files/ecommerce/__init__.py""")
path1 = Path(
    """9- Python Standard Library/4- Working with Files""")
print(path)
print(path.exists())
for p in path1.rglob("**"):
    print(p)
# path.rename("init.txt")
# path.unlink()
print(path.stat())
print(ctime(path.stat().st_ctime))
print(path.read_text())
with open(path, "r") as file:
    pass


path.write_text("print(\"__init__.py loaded\")")
print(path.read_text())
source = Path(
    """9- Python Standard Library/4- Working with Files/ecommerce/__init__.py""")
target = Path() / "init.py"

target.write_text(source.read_text())
shutil.copy(source, target)
