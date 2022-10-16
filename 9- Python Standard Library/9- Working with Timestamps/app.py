import time
print(time.time())


def send():
    for i in range(10000):
        pass


start = time.time()
send()
end = time.time()
delta = end-start
print(delta)
