
todos = []
n = int(input())

for _ in range(n):
    todos.append(input()) 

impostores = (input().split())

for j in range(len(todos)):
    if todos[j] not in impostores:
        print(todos[j], end=" ")
