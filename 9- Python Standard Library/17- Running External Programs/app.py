import subprocess


# com = subprocess.run(["powershell", "ls"], shell=True,
#                      capture_output=True, text=True, encoding="866")
# print(com.args)
# print(com.returncode)
# print(com.stderr)
# print(com.stdout)
# print(type(com))

try:
    com2 = subprocess.run(
        ["python", "9- Python Standard Library\\17- Running External Programs\\other.py"],
        shell=True,
        capture_output=True,
        text=True,
        check=True)
    print(com2.args)
    print(com2.stdout)
except subprocess.CalledProcessError as error:
    print(error)
