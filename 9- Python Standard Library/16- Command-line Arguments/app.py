import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("Use 'py app.py <pass>'")
else:
    password = sys.argv[1]
    print(password)
