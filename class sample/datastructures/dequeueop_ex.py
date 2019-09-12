from collections import deque
queue = deque(["Raju", "Deepu", "Navadeep", "Vamshi", "Vardhan"])
queue.append("ashish")           # Terry arrives
print(queue)
queue.append("swamy")          # Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
print(queue)
queue.pop()                 # The last to arrive now leaves
print(queue)
queue.popleft()                 # The second to arrive now leaves
print(queue)
                        # Remaining queue in order of arrival
