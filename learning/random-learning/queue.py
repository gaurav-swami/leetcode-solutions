from collections import deque

q = deque()

q.append(5)
q.append(6)
q.append(7)

print(q)


q.popleft()

print(q)

q.appendleft(8)

print(q)