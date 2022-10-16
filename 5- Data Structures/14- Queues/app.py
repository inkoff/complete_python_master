from collections import deque
# FIFO Last In First Out
[1, 2, 3]
[2, 3]  # -> 1
[3]  # -> 2
[]  # -> 3
# обратный эффект производительности от переиндексации списка
que = deque([])
que.append(1)
que.append(2)
que.append(3)
print(que)
que.popleft()
print(que)
if not que:
    print("empty")
