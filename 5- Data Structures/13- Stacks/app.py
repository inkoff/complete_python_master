# LIFO Last In First Out
[1, 2, 3]
[1, 2]  # -> 3
[1]  # -> 2
[]  # -> 1

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
if not browsing_session:
    print("redirect", browsing_session[-1])
    print("Disable back")
